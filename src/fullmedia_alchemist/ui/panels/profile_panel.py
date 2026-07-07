"""Left sidebar for Alchemist Profiles and Output Presets."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

from fullmedia_alchemist.profiles import DefaultContent
from fullmedia_alchemist.ui.widgets import CollapsibleSection, ToolButton


class ProfilePanel(QWidget):
    """Displays built-in/user Alchemist Profiles and Output Presets."""

    profile_selected = Signal(str)
    output_preset_selected = Signal(str)
    tool_hovered = Signal(str)
    tool_unhovered = Signal()

    def __init__(self, content: DefaultContent, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.content = content
        self.setObjectName("ProfilePanel")
        self.setMinimumWidth(280)

        header = QLabel("Profiles")
        header.setObjectName("PanelHeader")

        self.profile_list = QListWidget()
        self.profile_list.itemSelectionChanged.connect(self._emit_selected_profile)

        self.preset_list = QListWidget()
        self.preset_list.itemSelectionChanged.connect(self._emit_selected_preset)

        profile_actions = self._action_row()
        preset_actions = self._action_row()

        profile_section = CollapsibleSection("Alchemist Profiles", expanded=True)
        profile_section.add_widget(self.profile_list)
        profile_section.add_widget(profile_actions)

        preset_section = CollapsibleSection("Output Presets", expanded=True)
        preset_section.add_widget(self.preset_list)
        preset_section.add_widget(preset_actions)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.addWidget(header)
        layout.addWidget(profile_section)
        layout.addWidget(preset_section)
        layout.addStretch(1)

        self.reload(content)

    def reload(self, content: DefaultContent) -> None:
        """Reload panel lists from default content."""
        self.content = content
        self.profile_list.clear()
        self.preset_list.clear()

        for profile in content.profiles:
            item = QListWidgetItem(profile.profile_name)
            item.setData(256, profile.profile_id)
            item.setToolTip(f"{profile.profile_id}\n{profile.profile_version_id}\n{profile.description}")
            self.profile_list.addItem(item)

        for preset in content.output_presets:
            item = QListWidgetItem(f"{preset.preset_name} [{preset.format}]")
            item.setData(256, preset.preset_id)
            item.setToolTip(f"{preset.preset_id}\n{preset.preset_version_id}\n{preset.description}")
            self.preset_list.addItem(item)

        if self.profile_list.count():
            self.profile_list.setCurrentRow(0)

    def _action_row(self) -> QWidget:
        row = QWidget()
        layout = QHBoxLayout(row)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        actions = [
            ("＋", "Create new item", "profile_store"),
            ("⧉", "Duplicate selected item", "profile_store"),
            ("⇪", "Import", "profile_import_export"),
            ("⇩", "Export", "profile_import_export"),
            ("⚙", "Settings", "profile_validator"),
        ]
        for text, tooltip, tool_id in actions:
            button = ToolButton(text, tooltip=tooltip, tool_id=tool_id)
            button.tool_hovered.connect(self.tool_hovered)
            button.tool_unhovered.connect(self.tool_unhovered)
            layout.addWidget(button)

        return row

    def _emit_selected_profile(self) -> None:
        item = self.profile_list.currentItem()
        if item is not None:
            self.profile_selected.emit(str(item.data(256)))

    def _emit_selected_preset(self) -> None:
        item = self.preset_list.currentItem()
        if item is not None:
            self.output_preset_selected.emit(str(item.data(256)))
