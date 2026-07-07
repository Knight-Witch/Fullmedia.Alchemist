"""Allow `python -m fullmedia_alchemist` to launch the app."""

from __future__ import annotations

from .main import main


if __name__ == "__main__":
    raise SystemExit(main())
