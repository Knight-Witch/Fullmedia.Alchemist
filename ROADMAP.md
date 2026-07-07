# Roadmap

## Dev_v000.001.000_07-06-26 — Planning and scaffold

Goal: establish the project vocabulary, architecture, release model, and documentation baseline before coding.

Status: in progress.

Deliverables:

- README expansion.
- Project brief.
- Architecture plan.
- UI/UX specification.
- Profile and Output Preset schema planning.
- Import/export planning.
- Conversion engine planning.
- Versioning/footer planning.
- Build/release planning.

## MVP 1 — Application shell and profile foundation

Goal: create the first working PySide6 desktop shell with persistent JSON-backed profile/preset foundations.

Required scope:

- PySide6 main window.
- Modular collapsible panel layout.
- Left profile/preset sidebar.
- Center drag/drop queue area.
- Right inspector/preview panel.
- Bottom logs/progress panel.
- Footer/status bar with app version and internal tool hover metadata.
- App version visible in the UI.
- Icon asset system.
- Portable-mode path resolver.
- JSON profile and Output Preset model classes.
- Profile/preset validation.
- Profile duplicate action.
- Basic profile import/export shell.
- Advanced JSON editor tab with safe validation before save/import.
- Dev built-in Website Background Alchemist Profile.
- Dev built-in website background Output Presets.

Out of scope for MVP 1:

- Full updater implementation.
- Full installer.
- Full dependency-aware conversion graph.
- Public profile marketplace/discovery.

## MVP 2 — First real conversion workflows

Goal: wire real FFmpeg execution into the UI.

Required scope:

- Bundled FFmpeg/ffprobe path detection.
- Media probing via ffprobe.
- Website Background conversion workflow.
- Multi-size AV1 WebM outputs.
- VP9 WebM fallbacks.
- H.264 MP4 fallbacks.
- WebP poster generation.
- HDR/10-bit source skip guard.
- Color metadata preservation.
- Source migration after success only.
- Progress parsing.
- ETA and expected finish timestamp.
- Job logs.

## MVP 3 — GIF and PNG-series optimizer workflows

Goal: bring the legacy GIF/PNG-series scripts into the new engine.

Required scope:

- PNG sequence staging and natural sorting.
- GIF palette generation.
- Temporary test encode loop.
- Binary-search or candidate-search size targeting.
- Multiple GIF Output Presets from one source, such as 99 MB and 49 MB.
- WebP/WebM/MP4 outputs from PNG series.
- Naming history.
- Manual batch naming override.
- Collision detection and resolution.

## MVP 4 — Profile history and pack system

Goal: make user-created workflows safe to edit, roll back, and share.

Required scope:

- Profile version history.
- Output Preset version history.
- Rollback / roll-forward.
- Duplicate from historical version.
- Profile Bundle import/export.
- Output Preset Bundle import/export.
- Full Alchemist Pack import/export.
- Bundle dependency validation.
- Conflict handling and import summary.

## MVP 5 — Update and public release polish

Goal: prepare for public GitHub release.

Required scope:

- Check for updates button.
- GitHub Releases check.
- Download update flow.
- Installer/update helper decision.
- GitHub, Ko-fi, and Patreon icon links.
- Third-party license documentation.
- Portable ZIP release script.
- Public-safe default profile paths using variables/placeholders.
- User-facing documentation.
