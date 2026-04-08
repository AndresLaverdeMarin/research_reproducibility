"""Pydantic data models for the reproducibility pipeline."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Supporting enums
# ---------------------------------------------------------------------------

class FigureType(str, Enum):
    BAR_CHART = "bar_chart"
    LINE_PLOT = "line_plot"
    SCATTER = "scatter"
    HEATMAP = "heatmap"
    IMAGE_COMPARISON = "image_comparison"
    DIAGRAM = "diagram"
    OTHER = "other"


class DataAvailability(str, Enum):
    OPEN = "open"
    UPON_REQUEST = "upon_request"
    NOT_MENTIONED = "not_mentioned"


# ---------------------------------------------------------------------------
# PaperProfile components
# ---------------------------------------------------------------------------

class MethodologyStep(BaseModel):
    """A single step in the paper's methodology."""

    order: int
    description: str
    tools_mentioned: list[str] = Field(default_factory=list)
    data_inputs: list[str] = Field(default_factory=list)
    expected_outputs: list[str] = Field(default_factory=list)
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score based on source citation quality.",
    )


class Dataset(BaseModel):
    """A dataset referenced in the paper."""

    name: str
    url: str | None = None
    description: str = ""
    size_estimate: str | None = None
    licence: str | None = None
    availability: DataAvailability = DataAvailability.NOT_MENTIONED


class FigureToReproduce(BaseModel):
    """A figure that should be reproduced."""

    id: str
    caption: str = ""
    type: FigureType = FigureType.OTHER
    data_source: str = ""


class TableToReproduce(BaseModel):
    """A table that should be reproduced."""

    id: str
    caption: str = ""
    columns: list[str] = Field(default_factory=list)
    data_source: str = ""
    key_values: dict = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# PaperProfile -- main output of the Paper Analyst agent
# ---------------------------------------------------------------------------

class PaperProfile(BaseModel):
    """Structured representation of a research paper for reproduction."""

    doi: str | None = Field(default=None, description="Digital Object Identifier")
    title: str = Field(default="", description="Paper title")
    authors: list[str] = Field(default_factory=list, description="Author names")
    methodology_steps: list[MethodologyStep] = Field(
        default_factory=list, description="Ordered methodology steps"
    )
    datasets: list[Dataset] = Field(
        default_factory=list, description="Datasets referenced in the paper"
    )
    repository_links: list[str] = Field(
        default_factory=list, description="Code repository URLs found in the paper"
    )
    figures_to_reproduce: list[FigureToReproduce] = Field(
        default_factory=list, description="Figures targeted for reproduction"
    )
    tables_to_reproduce: list[TableToReproduce] = Field(
        default_factory=list, description="Tables targeted for reproduction"
    )
    hardware_requirements: str | None = Field(
        default=None, description="Stated hardware requirements"
    )
    stated_software_versions: dict[str, str] = Field(
        default_factory=dict, description="Software name to version mapping"
    )
    raw_analyst_responses: dict[str, str] = Field(
        default_factory=dict,
        description="Raw text responses from NotebookLM queries, keyed by query name",
    )


# ---------------------------------------------------------------------------
# Stubs for future agents (Retriever, Runner, Auditor)
# ---------------------------------------------------------------------------

class ArtefactInventory(BaseModel):
    """Output of the Artefact Retriever agent. To be implemented."""

    paper_doi: str | None = None


class ExecutionResult(BaseModel):
    """Output of the Execution Runner agent. To be implemented."""

    paper_doi: str | None = None


class ReproducibilityReport(BaseModel):
    """Output of the Validation Auditor agent. To be implemented."""

    paper_doi: str | None = None
    overall_score: float = Field(default=0.0, ge=0.0, le=100.0)
