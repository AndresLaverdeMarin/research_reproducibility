"""Client for Google NotebookLM via the notebooklm skill.

Wraps the NotebookLM skill scripts (ask_question.py, notebook_manager.py,
auth_manager.py) as subprocess calls. The skill handles browser automation,
persistent authentication, and anti-detection via Patchright.

Important: NotebookLM does not support programmatic paper upload. Papers
must be added manually to a NotebookLM notebook via the web UI, and the
notebook URL registered in the skill's library before querying.
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

_SKILL_DIR = Path.home() / ".claude" / "skills" / "notebooklm"
_RUN_SCRIPT = _SKILL_DIR / "scripts" / "run.py"

# The follow-up reminder the skill appends to every answer.
# We strip it since the pipeline handles its own query sequencing.
_FOLLOW_UP_SUFFIX = "\n\nEXTREMELY IMPORTANT: Is that ALL you need to know?"


class NotebookLMResponse(BaseModel):
    """A response from a NotebookLM query."""

    text: str
    citations: list[dict[str, Any]] = Field(default_factory=list)
    source_sections: list[str] = Field(default_factory=list)


class NotebookInfo(BaseModel):
    """Metadata for a registered NotebookLM notebook."""

    id: str
    url: str
    name: str = ""
    description: str = ""
    topics: list[str] = Field(default_factory=list)


class NotebookLMError(Exception):
    """Raised when a NotebookLM skill operation fails."""


class NotebookLMClient:
    """Client for querying Google NotebookLM via the notebooklm skill.

    The client delegates to the skill's CLI scripts which handle browser
    automation (Patchright), authentication, and stealth typing. Each
    query opens a headless browser session to the notebook URL.

    Usage::

        client = NotebookLMClient()
        client.connect()  # validates auth

        # Query a specific notebook by URL
        response = client.query(
            notebook_url="https://notebooklm.google.com/notebook/...",
            prompt="List the methodology steps.",
        )

        # Or query by notebook ID from the skill's library
        response = client.query(
            notebook_id="my-notebook",
            prompt="What datasets are referenced?",
        )

        client.close()
    """

    def __init__(self, headless: bool = True) -> None:
        self.headless = headless
        self._authenticated = False

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def connect(self) -> None:
        """Validate skill installation and that auth session is live.

        Checks the skill directory exists, then opens a headless browser
        to confirm the stored session can actually reach NotebookLM
        (not just that a state file exists on disk).

        Raises:
            NotebookLMError: If the skill is missing or the session is expired.
        """
        if not _SKILL_DIR.exists():
            raise NotebookLMError(
                f"NotebookLM skill not found at {_SKILL_DIR}. "
                "Install it under ~/.claude/skills/notebooklm/"
            )
        if not _RUN_SCRIPT.exists():
            raise NotebookLMError(
                f"Skill runner not found at {_RUN_SCRIPT}. "
                "The notebooklm skill may be incomplete."
            )

        # Quick file-existence check first (fast fail)
        result = self._run_skill("auth_manager.py", ["status"])
        if result.returncode != 0:
            raise NotebookLMError(
                "No stored auth found. Call authenticate() first."
            )

        # Real validation: open headless browser to confirm session is live
        result = self._run_skill("auth_manager.py", ["validate"], timeout=60)
        if result.returncode != 0:
            raise NotebookLMError(
                "NotebookLM session expired. Call authenticate() to re-login."
            )

        self._authenticated = True
        logger.info("NotebookLM client connected (auth validated).")

    def authenticate(self, headless: bool = False, timeout_minutes: int = 10) -> None:
        """Run interactive Google login for NotebookLM.

        Opens a Chromium browser window so the user can sign in to their
        Google account.  Once login succeeds the session cookies are
        persisted and subsequent ``connect()`` calls will pass.

        Args:
            headless: If False (default), shows the browser for manual login.
            timeout_minutes: How long to wait for the user to finish logging in.

        Raises:
            NotebookLMError: If the login times out or fails.
        """
        args = ["setup", f"--timeout={timeout_minutes}"]
        if headless:
            args.append("--headless")

        result = self._run_skill(
            "auth_manager.py",
            args,
            timeout=int(timeout_minutes * 60) + 30,
        )
        if result.returncode != 0:
            raise NotebookLMError(
                f"Authentication failed: {result.stderr.strip() or result.stdout.strip()}"
            )

        self._authenticated = True
        logger.info("NotebookLM authentication successful.")

    def close(self) -> None:
        """Mark the client as disconnected."""
        self._authenticated = False

    @property
    def is_connected(self) -> bool:
        return self._authenticated

    # ------------------------------------------------------------------
    # Querying
    # ------------------------------------------------------------------

    def query(
        self,
        prompt: str,
        notebook_url: str | None = None,
        notebook_id: str | None = None,
    ) -> NotebookLMResponse:
        """Send a query to a NotebookLM notebook.

        NotebookLM only answers from the uploaded document, ensuring
        source-grounded responses with no hallucinated content.

        Provide either ``notebook_url`` or ``notebook_id``. If neither is
        given, the skill's active notebook is used.

        Args:
            prompt: The query text.
            notebook_url: Direct URL to a NotebookLM notebook.
            notebook_id: Notebook ID from the skill's library.

        Returns:
            NotebookLMResponse with the answer text.

        Raises:
            NotebookLMError: If the query fails or times out.
        """
        self._require_connected()

        args = ["--question", prompt]
        if notebook_url:
            args.extend(["--notebook-url", notebook_url])
        elif notebook_id:
            args.extend(["--notebook-id", notebook_id])

        if not self.headless:
            args.append("--show-browser")

        result = self._run_skill("ask_question.py", args, timeout=180)

        if result.returncode != 0:
            raise NotebookLMError(
                f"NotebookLM query failed (exit {result.returncode}): "
                f"{result.stderr.strip()}"
            )

        answer = self._parse_answer(result.stdout)
        if not answer:
            raise NotebookLMError(
                "NotebookLM returned no answer. Check that the notebook "
                "URL is correct and the paper has been uploaded."
            )

        return NotebookLMResponse(text=answer)

    # ------------------------------------------------------------------
    # Notebook library management
    # ------------------------------------------------------------------

    def list_notebooks(self) -> list[NotebookInfo]:
        """List all notebooks registered in the skill's library."""
        data = self._read_library()
        if not data:
            return []
        return [
            self._parse_notebook_info(key, nb)
            for key, nb in data.get("notebooks", {}).items()
        ]

    def get_active_notebook(self) -> NotebookInfo | None:
        """Return the currently active notebook, if any."""
        data = self._read_library()
        if not data:
            return None

        active_id = data.get("active_notebook_id")
        if not active_id:
            return None

        nb = data.get("notebooks", {}).get(active_id)
        if not nb:
            return None

        return self._parse_notebook_info(active_id, nb)

    def add_notebook(
        self,
        url: str,
        name: str,
        description: str,
        topics: list[str],
    ) -> None:
        """Register a notebook in the skill's library.

        The paper must already be uploaded to NotebookLM via the web UI.

        Args:
            url: NotebookLM notebook URL.
            name: Display name.
            description: What the notebook contains.
            topics: List of topic tags.
        """
        args = [
            "add",
            "--url", url,
            "--name", name,
            "--description", description,
            "--topics", ",".join(topics),
        ]
        result = self._run_skill("notebook_manager.py", args)
        if result.returncode != 0:
            raise NotebookLMError(
                f"Failed to add notebook: {result.stderr.strip()}"
            )

    def activate_notebook(self, notebook_id: str) -> None:
        """Set a notebook as the active default."""
        result = self._run_skill(
            "notebook_manager.py", ["activate", "--id", notebook_id]
        )
        if result.returncode != 0:
            raise NotebookLMError(
                f"Failed to activate notebook: {result.stderr.strip()}"
            )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _read_library() -> dict[str, Any] | None:
        """Read the skill's notebook library file."""
        library_file = _SKILL_DIR / "data" / "library.json"
        if not library_file.exists():
            return None
        return json.loads(library_file.read_text())

    @staticmethod
    def _parse_notebook_info(key: str, nb: dict[str, Any]) -> NotebookInfo:
        """Build a NotebookInfo from a raw library entry."""
        return NotebookInfo(
            id=nb.get("id", key),
            url=nb.get("url", ""),
            name=nb.get("name", ""),
            description=nb.get("description", ""),
            topics=nb.get("topics", []),
        )

    def _require_connected(self) -> None:
        if not self._authenticated:
            raise NotebookLMError(
                "Client not connected. Call connect() first."
            )

    def _run_skill(
        self,
        script: str,
        args: list[str] | None = None,
        timeout: int = 120,
    ) -> subprocess.CompletedProcess[str]:
        """Run a skill script via the run.py wrapper.

        Args:
            script: Script filename (e.g. "ask_question.py").
            args: CLI arguments to pass to the script.
            timeout: Maximum seconds to wait.

        Returns:
            CompletedProcess with stdout and stderr captured.
        """
        cmd = [sys.executable, str(_RUN_SCRIPT), script] + (args or [])
        logger.debug("Running skill: %s", " ".join(cmd))

        try:
            return subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(_SKILL_DIR),
            )
        except subprocess.TimeoutExpired as exc:
            raise NotebookLMError(
                f"Skill script {script} timed out after {timeout}s"
            ) from exc

    @staticmethod
    def _parse_answer(stdout: str) -> str:
        """Extract the answer text from ask_question.py stdout.

        The skill prints status lines prefixed with emoji, then the
        answer between separator lines. We also strip the follow-up
        reminder the skill appends.
        """
        # The answer appears after the last "=" separator block
        sections = stdout.split("=" * 60)
        if len(sections) >= 3:
            # sections: [preamble, "Question: ...", answer, trailing]
            raw_answer = sections[2].strip()
        else:
            # Fallback: take everything after the last status line
            lines = stdout.strip().splitlines()
            answer_lines = [
                line for line in lines
                if not line.startswith("  ") or not any(
                    c in line for c in "\U0001f4ac\U0001f4da\U0001f310\u23f3\u2713\U0001f4e4\u2705\u274c\U0001f527"
                )
            ]
            raw_answer = "\n".join(answer_lines).strip()

        # Strip the follow-up reminder the skill appends
        idx = raw_answer.find(_FOLLOW_UP_SUFFIX)
        if idx != -1:
            raw_answer = raw_answer[:idx].strip()

        return raw_answer
