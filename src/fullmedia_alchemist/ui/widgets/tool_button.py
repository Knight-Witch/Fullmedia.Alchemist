"""Tool-aware button that emits footer metadata hover signals."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QEnterEvent
from PySide6.QtWidgets import QPushButton, QWidget


class ToolButton(QPushButton):
    """Small button with an internal tool metadata identifier."""

    tool_hovered = Signal(str)
    tool_unhovered = Signal()

    def __init__(
        self,
        text: str,
        *,
        tool_id: str | None = None,
        tooltip: str | None = None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(text, parent)
        self.tool_id = tool_id
        if tool_id:
            self.setProperty("tool_id", tool_id)
        if tooltip:
            self.setToolTip(tooltip)

    def enterEvent(self, event: QEnterEvent) -> None:  # noqa: N802 - Qt override
        if self.tool_id:
            self.tool_hovered.emit(self.tool_id)
        super().enterEvent(event)

    def leaveEvent(self, event) -> None:  # noqa: N802 - Qt override
        self.tool_unhovered.emit()
        super().leaveEvent(event)
