"""Application entry point for Fullmedia Alchemist."""

from __future__ import annotations

from fullmedia_alchemist.ui.main_window import run_app


def main() -> int:
    """Run the PySide6 application."""
    return run_app()


if __name__ == "__main__":
    raise SystemExit(main())
