"""Footer/status bar widget with app and internal tool version metadata."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QWidget

from fullmedia_alchemist.core.tool_registry import get_tool_metadata
from fullmedia_alchemist.version import APP_NAME, APP_VERSION


class FooterStatusBar(QFrame):
    """Subtle footer showing app state and hover tool metadata."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("FooterStatusBar")
        self.setFrameShape(QFrame.Shape.StyledPanel)

        self.state_label = QLabel("Ready")
        self.tool_label = QLabel("")
        self.tool_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.version_label = QLabel(f"{APP_NAME} • {APP_VERSION}")
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 3, 8, 3)
        layout.setSpacing(12)
        layout.addWidget(self.state_label, 1)
        layout.addWidget(self.tool_label, 3)
        layout.addWidget(self.version_label, 1)

    def set_state(self, text: str) -> None:
        """Set left-side app state text."""
        self.state_label.setText(text)

    def show_tool(self, tool_id: str | None) -> None:
        """Display registered internal tool metadata by ID."""
        if not tool_id:
            self.tool_label.clear()
            return

        metadata = get_tool_metadata(tool_id)
        if metadata is None:
            self.tool_label.setText(tool_id)
            return

        self.tool_label.setText(
            f"{metadata.name} • {metadata.tool_id} • {metadata.version} • {metadata.description}"
        )

    def clear_tool(self) -> None:
        """Clear hover metadata."""
        self.tool_label.clear()
