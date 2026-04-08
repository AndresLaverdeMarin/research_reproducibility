"""Append-only reproducibility ledger.

Every action, decision, and output in the pipeline is logged here
as a JSON-lines file for full audit trail.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


_DEFAULT_LEDGER_PATH = Path("repro_ledger.jsonl")


class Ledger:
    """Append-only structured log for reproducibility auditing."""

    def __init__(self, path: Path = _DEFAULT_LEDGER_PATH) -> None:
        self.path = path

    def append(
        self,
        phase: str,
        action: str,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Append an entry to the ledger and return it."""
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "phase": phase,
            "action": action,
            "data": data or {},
        }
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry

    def read(
        self,
        phase: str | None = None,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        """Read ledger entries, optionally filtered by phase."""
        if not self.path.exists():
            return []
        entries = []
        with open(self.path) as f:
            for line in f:
                entry = json.loads(line)
                if phase and entry.get("phase") != phase:
                    continue
                entries.append(entry)
        if limit:
            entries = entries[-limit:]
        return entries

    def export(self, output_format: str = "json") -> str:
        """Export the full ledger as a JSON array string."""
        entries = self.read()
        if output_format == "json":
            return json.dumps(entries, indent=2)
        raise ValueError(f"Unsupported export format: {output_format}")
