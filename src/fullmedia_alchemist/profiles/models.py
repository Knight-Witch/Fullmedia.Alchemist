"""Lightweight models used by the MVP 1 UI shell.

These are intentionally narrow summary models. Full pydantic validation models will replace or
extend these after the PySide6 shell is in place.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class OutputPresetSummary:
    """Summary information for one Output Preset JSON file."""

    preset_id: str
    preset_name: str
    preset_version_id: str
    format: str
    description: str
    path: Path
    raw: dict[str, Any] = field(repr=False)


@dataclass(frozen=True)
class AlchemistProfileSummary:
    """Summary information for one Alchemist Profile JSON file."""

    profile_id: str
    profile_name: str
    profile_version_id: str
    description: str
    path: Path
    output_preset_ids: tuple[str, ...]
    raw: dict[str, Any] = field(repr=False)


@dataclass(frozen=True)
class ValidationIssue:
    """Simple validation issue used before formal schema validation exists."""

    path: Path
    message: str
