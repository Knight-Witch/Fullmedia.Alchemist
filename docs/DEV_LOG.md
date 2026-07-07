# Dev Log

## Dev_v000.001.000_07-06-26

Focus: project planning, documentation scaffold, and first MVP 1 UI shell implementation.

Created the initial repository documentation set for Fullmedia Alchemist.

Captured confirmed decisions:

- App name: Fullmedia Alchemist.
- Repo: `Fullmedia.Alchemist`.
- Executable: `Fullmedia_Alchemist.exe`.
- Windows local desktop app.
- PySide6 UI.
- FFmpeg/ffprobe backend.
- Portable ZIP first.
- Directly bundled FFmpeg/ffprobe.
- JSON for profile/preset code format.
- No executable profile scripts.
- Other repos are reference-only.
- Alchemist Profile and Output Preset terminology.
- Bundle/pack terminology.
- Icon-forward modular UI.
- Footer/status bar internal tool version metadata.
- First real workflow: Website Background conversion.

Implemented in first coding pass:

- Initial Python project scaffold.
- App version constants.
- Internal tool metadata registry.
- Lightweight profile/preset summary models.
- Default JSON loader for built-in Alchemist Profiles and Output Presets.
- Minimal reference validation for missing required fields and profile preset references.
- PySide6 main window shell.
- Main UI layout: left profile/preset panel, center queue panel, right inspector/preview panel, bottom progress/log panel, footer/status bar.
- Reusable collapsible section widget.
- Reusable drag/drop zone widget.
- Reusable footer/status bar widget.
- Reusable tool-aware button widget for footer hover metadata.
- Entry point now launches the PySide6 shell instead of console placeholder output.
- Initial tests for app metadata and default profile/preset loading.

Next coding step:

- Add proper reusable drag/drop path field widgets.
- Add profile/preset store shell.
- Add Advanced JSON editor shell.
- Add import/export shell.
- Add portable path resolver shell.
- Begin formal validation models for profiles and Output Presets.
