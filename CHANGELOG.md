# Changelog

All notable Fullmedia Alchemist changes should be recorded here.

Dev builds use the format:

```text
Dev_vxxx.xxx.xxx_mm-dd-yy
```

Example:

```text
Dev_v000.001.000_07-06-26
```

## Dev_v000.001.000_07-06-26

Initial planning, repository documentation scaffold, and first MVP 1 application shell implementation.

Added:

- Expanded README with the project concept, terminology, and release model.
- Roadmap with staged MVPs.
- Project documentation scaffold under `docs/`.
- Comprehensive `docs/DEVELOPMENT_CHECKLIST.md`.
- Confirmed JSON as the v0 profile/preset code format.
- Confirmed portable ZIP as the first release mode.
- Confirmed directly bundled FFmpeg/ffprobe for release packages.
- Confirmed active development is limited to `Fullmedia.Alchemist`; other repos are reference/assets-only.
- Confirmed Profile/Output Preset/Bundle/Pack terminology.
- Confirmed icon-first modular PySide6 UI direction.
- Confirmed footer/status bar internal tool versioning requirement.
- Added initial Python package scaffold.
- Added app version constants.
- Added internal tool registry.
- Added lightweight default profile/preset loader.
- Added lightweight profile/preset summary models.
- Added MVP PySide6 main window shell.
- Added modular panels for profiles/presets, queue, inspector/preview, and progress/logs.
- Added reusable collapsible section widget.
- Added reusable drop zone widget.
- Added footer/status bar widget.
- Added tool-aware button widget for footer hover metadata.
- Replaced console placeholder entry point with PySide6 app launch.
- Added default loader tests.
