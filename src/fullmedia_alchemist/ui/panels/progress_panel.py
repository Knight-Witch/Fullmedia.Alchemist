"""Bottom progress/logs panel."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QPlainTextEdit, QProgressBar, QVBoxLayout, QWidget

from fullmedia_alchemist.ui.widgets import CollapsibleSection


class ProgressPanel(QWidget):
    """Displays current progress and log output."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("ProgressPanel")
        self.setMinimumHeight(170)

        self.current_label = QLabel("No active job.")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")

        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setMaximumBlockCount(2000)
        self.log_view.appendPlainText("Fullmedia Alchemist log initialized.")

        progress_section = CollapsibleSection("Progress", expanded=True)
        progress_section.add_widget(self.current_label)
        progress_section.add_widget(self.progress_bar)

        log_section = CollapsibleSection("Logs", expanded=True)
        log_section.add_widget(self.log_view)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 8)
        layout.setSpacing(6)
        layout.addWidget(progress_section)
        layout.addWidget(log_section, 1)

    def append_log(self, message: str) -> None:
        """Append one line to the log view."""
        self.log_view.appendPlainText(message)

    def set_status(self, message: str, percent: int | None = None) -> None:
        """Set current progress message and optionally progress percent."""
        self.current_label.setText(message)
        if percent is not None:
            self.progress_bar.setValue(max(0, min(100, percent)))
