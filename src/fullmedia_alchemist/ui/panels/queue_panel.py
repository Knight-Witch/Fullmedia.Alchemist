"""Center queue panel with drag/drop intake."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

from fullmedia_alchemist.ui.widgets import DropZone


class QueuePanel(QWidget):
    """Displays queued files/folders for future conversion jobs."""

    paths_added = Signal(list)
    tool_hovered = Signal(str)
    tool_unhovered = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("QueuePanel")

        header = QLabel("Conversion Queue")
        header.setObjectName("PanelHeader")

        self.drop_zone = DropZone("Drop source files, folders, or archives here\n\nBrowse buttons will be wired next.")
        self.drop_zone.paths_dropped.connect(self.add_paths)
        self.drop_zone.setProperty("tool_id", "app_shell")
        self.drop_zone.enterEvent = lambda event: self.tool_hovered.emit("app_shell")  # type: ignore[method-assign]
        self.drop_zone.leaveEvent = lambda event: self.tool_unhovered.emit()  # type: ignore[method-assign]

        self.queue_list = QListWidget()

        button_row = QHBoxLayout()
        self.start_button = QPushButton("▶ Start")
        self.pause_button = QPushButton("⏸ Pause")
        self.stop_button = QPushButton("■ Stop")
        for button, tool_id in [
            (self.start_button, "conversion_engine"),
            (self.pause_button, "conversion_engine"),
            (self.stop_button, "conversion_engine"),
        ]:
            button.setProperty("tool_id", tool_id)
            button.enterEvent = lambda event, tid=tool_id: self.tool_hovered.emit(tid)  # type: ignore[method-assign]
            button.leaveEvent = lambda event: self.tool_unhovered.emit()  # type: ignore[method-assign]
            button_row.addWidget(button)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.addWidget(header)
        layout.addWidget(self.drop_zone)
        layout.addWidget(self.queue_list, 1)
        layout.addLayout(button_row)

    def add_paths(self, paths: list[str]) -> None:
        """Add dropped paths to the visible queue."""
        for raw_path in paths:
            path = Path(raw_path)
            label = f"{'Folder' if path.is_dir() else 'File'} • {path.name}"
            item = QListWidgetItem(label)
            item.setToolTip(str(path))
            item.setData(256, str(path))
            self.queue_list.addItem(item)

        if paths:
            self.paths_added.emit(paths)
