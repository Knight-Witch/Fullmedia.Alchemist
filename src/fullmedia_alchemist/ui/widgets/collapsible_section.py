"""Collapsible section widget used by profile/editor panels."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class CollapsibleSection(QFrame):
    """Small reusable collapsible container.

    This is intentionally simple for MVP 1. Later passes can add animation, icons, and
    persisted expanded/collapsed state.
    """

    def __init__(self, title: str, *, expanded: bool = True, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._expanded = expanded

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setObjectName("CollapsibleSection")

        self.toggle_button = QPushButton("▾" if expanded else "▸")
        self.toggle_button.setFixedWidth(28)
        self.toggle_button.setToolTip(f"Collapse or expand {title}")
        self.toggle_button.clicked.connect(self.toggle)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("SectionTitle")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        header = QHBoxLayout()
        header.setContentsMargins(4, 4, 4, 4)
        header.addWidget(self.toggle_button)
        header.addWidget(self.title_label, 1)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(8, 6, 8, 8)
        self.content_layout.setSpacing(6)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(header)
        main_layout.addWidget(self.content_widget)

        self.content_widget.setVisible(expanded)

    def add_widget(self, widget: QWidget) -> None:
        """Add a widget to the content area."""
        self.content_layout.addWidget(widget)

    def toggle(self) -> None:
        """Toggle expanded/collapsed state."""
        self._expanded = not self._expanded
        self.content_widget.setVisible(self._expanded)
        self.toggle_button.setText("▾" if self._expanded else "▸")

    @property
    def expanded(self) -> bool:
        """Return current expanded state."""
        return self._expanded
