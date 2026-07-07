"""Load built-in Alchemist Profiles and Output Presets from JSON files."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .models import AlchemistProfileSummary, OutputPresetSummary, ValidationIssue


@dataclass(frozen=True)
class DefaultContent:
    """Loaded built-in profiles, presets, and validation issues."""

    profiles: tuple[AlchemistProfileSummary, ...]
    output_presets: tuple[OutputPresetSummary, ...]
    issues: tuple[ValidationIssue, ...]
    defaults_root: Path

    @property
    def is_valid(self) -> bool:
        """Return True when no validation issues were found."""
        return not self.issues


def find_repo_root(start: Path | None = None) -> Path:
    """Find the repository root by walking upward from this file."""
    current = (start or Path(__file__)).resolve()
    for parent in [current, *current.parents]:
        if (parent / "profiles" / "defaults").exists():
            return parent
    return Path.cwd()


def defaults_root() -> Path:
    """Return the expected built-in defaults directory."""
    return find_repo_root() / "profiles" / "defaults"


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    return data


def _required_str(data: dict[str, Any], key: str, path: Path, issues: list[ValidationIssue]) -> str:
    value = data.get(key)
    if isinstance(value, str) and value.strip():
        return value
    issues.append(ValidationIssue(path, f"Missing or invalid string field: {key}"))
    return ""


def _load_output_preset(path: Path, issues: list[ValidationIssue]) -> OutputPresetSummary | None:
    try:
        data = _read_json(path)
    except Exception as exc:  # pragma: no cover - defensive loader path
        issues.append(ValidationIssue(path, f"Could not read JSON: {exc}"))
        return None

    if data.get("kind") != "output_preset":
        issues.append(ValidationIssue(path, "Expected kind='output_preset'"))
        return None

    preset_id = _required_str(data, "preset_id", path, issues)
    preset_name = _required_str(data, "preset_name", path, issues)
    preset_version_id = _required_str(data, "preset_version_id", path, issues)
    format_name = _required_str(data, "format", path, issues)
    description = data.get("description", "")
    if not isinstance(description, str):
        description = ""

    if not all([preset_id, preset_name, preset_version_id, format_name]):
        return None

    return OutputPresetSummary(
        preset_id=preset_id,
        preset_name=preset_name,
        preset_version_id=preset_version_id,
        format=format_name,
        description=description,
        path=path,
        raw=data,
    )


def _load_profile(path: Path, issues: list[ValidationIssue]) -> AlchemistProfileSummary | None:
    try:
        data = _read_json(path)
    except Exception as exc:  # pragma: no cover - defensive loader path
        issues.append(ValidationIssue(path, f"Could not read JSON: {exc}"))
        return None

    if data.get("kind") != "alchemist_profile":
        issues.append(ValidationIssue(path, "Expected kind='alchemist_profile'"))
        return None

    profile_id = _required_str(data, "profile_id", path, issues)
    profile_name = _required_str(data, "profile_name", path, issues)
    profile_version_id = _required_str(data, "profile_version_id", path, issues)
    description = data.get("description", "")
    if not isinstance(description, str):
        description = ""

    outputs = data.get("outputs", [])
    output_preset_ids: list[str] = []
    if isinstance(outputs, list):
        for index, item in enumerate(outputs):
            if not isinstance(item, dict):
                issues.append(ValidationIssue(path, f"outputs[{index}] must be an object"))
                continue
            output_preset_id = item.get("output_preset_id")
            if isinstance(output_preset_id, str) and output_preset_id.strip():
                output_preset_ids.append(output_preset_id)
            else:
                issues.append(
                    ValidationIssue(path, f"outputs[{index}].output_preset_id is missing")
                )
    else:
        issues.append(ValidationIssue(path, "outputs must be a list"))

    if not all([profile_id, profile_name, profile_version_id]):
        return None

    return AlchemistProfileSummary(
        profile_id=profile_id,
        profile_name=profile_name,
        profile_version_id=profile_version_id,
        description=description,
        path=path,
        output_preset_ids=tuple(output_preset_ids),
        raw=data,
    )


def load_default_content(root: Path | None = None) -> DefaultContent:
    """Load built-in profiles/presets and run a minimal reference validation pass."""
    root = root or defaults_root()
    issues: list[ValidationIssue] = []

    preset_dir = root / "output_presets"
    profile_dir = root / "alchemist_profiles"

    output_presets = tuple(
        preset
        for path in sorted(preset_dir.glob("*.fma-output-preset.json"))
        if (preset := _load_output_preset(path, issues)) is not None
    )

    profiles = tuple(
        profile
        for path in sorted(profile_dir.glob("*.fma-profile.json"))
        if (profile := _load_profile(path, issues)) is not None
    )

    preset_ids = {preset.preset_id for preset in output_presets}
    for profile in profiles:
        for preset_id in profile.output_preset_ids:
            if preset_id not in preset_ids:
                issues.append(
                    ValidationIssue(
                        profile.path,
                        f"Profile references missing Output Preset: {preset_id}",
                    )
                )

    return DefaultContent(
        profiles=profiles,
        output_presets=output_presets,
        issues=tuple(issues),
        defaults_root=root,
    )
