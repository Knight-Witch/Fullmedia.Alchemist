# Next Steps

## Immediate next implementation task

Build MVP 1 application shell.

Required first coding pass:

1. Create PySide6 main window.
2. Add visible app version.
3. Add bottom footer/status bar.
4. Wire footer to internal tool registry hover metadata.
5. Create left profile/preset panel.
6. Create center drag/drop queue panel.
7. Create right inspector/preview placeholder panel.
8. Create bottom progress/logs panel.
9. Load default Alchemist Profiles and Output Presets from JSON.
10. Add basic validation pass for default JSON.

## After shell exists

1. Implement profile/preset store.
2. Implement profile duplicate.
3. Implement profile import/export shell.
4. Implement Advanced JSON editor with schema validation.
5. Implement portable path resolver.
6. Implement FFmpeg/ffprobe detection.
7. Wire Website Background conversion as first real workflow.

## Known non-blocking decisions

- Installer design can wait.
- Full updater can wait.
- Full dependency-aware conversion graph can wait, but schema should not block it.
- Public release license audit can wait until before public binary distribution.

## Current conflict check

No blocking direction conflicts identified.

Clarification recorded:

Bundled FFmpeg means bundled into release packages so users do not need separate installation. The repo currently ignores raw `vendor/ffmpeg/*.exe` to avoid accidental large binary commits until a deliberate packaging decision is made.
