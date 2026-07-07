"""Right-side inspector/preview panel."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget

from fullmedia_alchemist.profiles import DefaultContent
from fullmedia_alchemist.ui.widgets import CollapsibleSection


class InspectorPanel(QWidget):
    """Displays selected profile/preset/job details."""

    def __init__(self, content: DefaultContent, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.content = content
        self.setObjectName("InspectorPanel")
        self.setMinimumWidth(320)

        header = QLabel("Inspector")
        header.setObjectName("PanelHeader")

        self.preview_label = QLabel("Preview / thumbnail area")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_label.setMinimumHeight(160)
        self.preview_label.setObjectName("PreviewPlaceholder")

        self.details = QTextEdit()
        self.details.setReadOnly(True)
        self.details.setPlaceholderText("Select a profile, preset, or queued item.")

        preview_section = CollapsibleSection("Preview", expanded=True)
        preview_section.add_widget(self.preview_label)

        details_section = CollapsibleSection("Details", expanded=True)
        details_section.add_widget(self.details)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.addWidget(header)
        layout.addWidget(preview_section)
        layout.addWidget(details_section, 1)

    def show_profile(self, profile_id: str) -> None:
        """Show profile details by ID."""
        profile = next((p for p in self.content.profiles if p.profile_id == profile_id), None)
        if profile is None:
            return

        outputs = "\n".join(f"- {preset_id}" for preset_id in profile.output_preset_ids)
        self.details.setPlainText(
            f"Alchemist Profile\n"
            f"Name: {profile.profile_name}\n"
            f"ID: {profile.profile_id}\n"
            f"Version: {profile.profile_version_id}\n\n"
            f"Description:\n{profile.description}\n\n"
            f"Output Presets:\n{outputs or '- None'}\n\n"
            f"File:\n{profile.path}"
        )

    def show_output_preset(self, preset_id: str) -> None:
        """Show Output Preset details by ID."""
        preset = next((p for p in self.content.output_presets if p.preset_id == preset_id), None)
        if preset is None:
            return

        self.details.setPlainText(
            f"Output Preset\n"
            f"Name: {preset.preset_name}\n"
            f"ID: {preset.preset_id}\n"
            f"Version: {preset.preset_version_id}\n"
            f"Format: {preset.format}\n\n"
            f"Description:\n{preset.description}\n\n"
            f"File:\n{preset.path}"
        )

    def show_queue_paths(self, paths: list[str]) -> None:
        """Show recently added queue paths."""
        self.details.setPlainText("Queued path(s):\n" + "\n".join(paths))
