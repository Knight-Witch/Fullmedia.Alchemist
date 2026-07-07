# Current Status

## Current dev version

```text
Dev_v000.001.000_07-06-26
```

## Current implementation state

The project has moved from planning-only into MVP 1 shell implementation.

Completed in the first coding pass:

- Python package scaffold exists under `src/fullmedia_alchemist/`.
- Main entry point launches the PySide6 application shell.
- App version constants exist in `version.py`.
- Internal tool metadata registry exists in `core/tool_registry.py`.
- Built-in profile/preset JSON loader exists.
- Lightweight Alchemist Profile and Output Preset summary models exist.
- Minimal built-in JSON validation exists.
- Main PySide6 window exists.
- Main layout exists:
  - Left profile/preset panel.
  - Center queue/drop panel.
  - Right inspector/preview panel.
  - Bottom progress/log panel.
  - Footer/status bar.
- Reusable widgets exist:
  - Collapsible section.
  - Drop zone.
  - Footer/status bar.
  - Tool-aware button.
- Default Website Background profile and presets are loaded/displayed by the shell.
- Tests exist for app version metadata and default content loading.

## Not implemented yet

- Real profile/preset persistence beyond loading built-in defaults.
- Full pydantic schema validation.
- Profile/preset editor UI.
- Advanced JSON editor.
- Import/export UI and logic.
- Drag/drop path field widget for source/output/archive fields.
- Portable path resolver.
- FFmpeg/ffprobe detection.
- Any actual conversion execution.
- Website Background conversion modules.
- GIF optimizer.
- PNG series processor.

## Immediate next coding tasks

1. Add reusable drag/drop path field widget with browse button.
2. Add portable path resolver shell.
3. Add formal pydantic models for built-in Alchemist Profiles and Output Presets.
4. Replace lightweight validation with schema validation.
5. Add profile/preset store shell.
6. Add Advanced JSON editor shell.
7. Add import/export shell.
8. Add FFmpeg/ffprobe detection.
