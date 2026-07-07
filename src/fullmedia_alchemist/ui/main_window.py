"""Main PySide6 window for Fullmedia Alchemist."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QSplitter, QVBoxLayout, QWidget

from fullmedia_alchemist.profiles import DefaultContent, load_default_content
from fullmedia_alchemist.ui.panels import InspectorPanel, ProfilePanel, ProgressPanel, QueuePanel
from fullmedia_alchemist.ui.widgets import FooterStatusBar
from fullmedia_alchemist.version import APP_NAME, APP_VERSION


class MainWindow(QMainWindow):
    """MVP 1 application shell.

    This class establishes the permanent UI shape before conversion execution is wired in.
    """

    def __init__(self, content: DefaultContent | None = None) -> None:
        super().__init__()
        self.content = content or load_default_content()

        self.setWindowTitle(f"{APP_NAME} — {APP_VERSION}")
        self.resize(1480, 900)
        self.setMinimumSize(1100, 720)

        self.profile_panel = ProfilePanel(self.content)
        self.queue_panel = QueuePanel()
        self.inspector_panel = InspectorPanel(self.content)
        self.progress_panel = ProgressPanel()
        self.footer = FooterStatusBar()

        self._build_layout()
        self._wire_signals()
        self._apply_base_style()
        self._show_startup_status()

    def _build_layout(self) -> None:
        header = QLabel(f"{APP_NAME}  •  {APP_VERSION}")
        header.setObjectName("AppHeader")
        header.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        top_splitter = QSplitter(Qt.Orientation.Horizontal)
        top_splitter.addWidget(self.profile_panel)
        top_splitter.addWidget(self.queue_panel)
        top_splitter.addWidget(self.inspector_panel)
        top_splitter.setSizes([310, 760, 410])
        top_splitter.setChildrenCollapsible(False)

        vertical_splitter = QSplitter(Qt.Orientation.Vertical)
        vertical_splitter.addWidget(top_splitter)
        vertical_splitter.addWidget(self.progress_panel)
        vertical_splitter.setSizes([680, 220])
        vertical_splitter.setChildrenCollapsible(False)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(8, 8, 8, 6)
        layout.setSpacing(6)
        layout.addWidget(header)
        layout.addWidget(vertical_splitter, 1)
        layout.addWidget(self.footer)

        self.setCentralWidget(central)

    def _wire_signals(self) -> None:
        self.profile_panel.profile_selected.connect(self.inspector_panel.show_profile)
        self.profile_panel.output_preset_selected.connect(self.inspector_panel.show_output_preset)
        self.profile_panel.tool_hovered.connect(self.footer.show_tool)
        self.profile_panel.tool_unhovered.connect(self.footer.clear_tool)

        self.queue_panel.paths_added.connect(self.inspector_panel.show_queue_paths)
        self.queue_panel.paths_added.connect(self._queue_paths_added)
        self.queue_panel.tool_hovered.connect(self.footer.show_tool)
        self.queue_panel.tool_unhovered.connect(self.footer.clear_tool)

    def _show_startup_status(self) -> None:
        self.progress_panel.append_log(f"Loaded defaults from: {self.content.defaults_root}")
        self.progress_panel.append_log(
            f"Loaded {len(self.content.profiles)} Alchemist Profile(s) and "
            f"{len(self.content.output_presets)} Output Preset(s)."
        )

        if self.content.issues:
            self.footer.set_state("Defaults loaded with warnings")
            for issue in self.content.issues:
                self.progress_panel.append_log(f"WARNING: {issue.path}: {issue.message}")
            QMessageBox.warning(
                self,
                "Default profile validation warnings",
                "One or more built-in profiles/presets loaded with warnings. "
                "Check the log panel for details.",
            )
        else:
            self.footer.set_state("Ready")
            self.progress_panel.append_log("Default profile/preset validation passed.")

    def _queue_paths_added(self, paths: list[str]) -> None:
        self.footer.set_state(f"Queued {len(paths)} item(s)")
        self.progress_panel.append_log(f"Queued {len(paths)} path(s).")
        for path in paths:
            self.progress_panel.append_log(f"  {path}")

    def _apply_base_style(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow, QWidget {
                font-family: Segoe UI, Arial, sans-serif;
                font-size: 10pt;
            }
            QLabel#AppHeader {
                font-size: 13pt;
                font-weight: 600;
                padding: 4px 6px;
            }
            QLabel#PanelHeader {
                font-size: 11pt;
                font-weight: 600;
                padding: 2px;
            }
            QLabel#SectionTitle {
                font-weight: 600;
            }
            QFrame#CollapsibleSection {
                border: 1px solid rgba(127, 127, 127, 0.35);
                border-radius: 6px;
            }
            QWidget#DropZone {
                border: 2px dashed rgba(127, 127, 127, 0.65);
                border-radius: 10px;
            }
            QLabel#PreviewPlaceholder {
                border: 1px solid rgba(127, 127, 127, 0.35);
                border-radius: 8px;
            }
            QFrame#FooterStatusBar {
                border: 1px solid rgba(127, 127, 127, 0.25);
                border-radius: 4px;
            }
            """
        )


def run_app() -> int:
    """Launch the PySide6 application."""
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    window.show()
    return app.exec()
