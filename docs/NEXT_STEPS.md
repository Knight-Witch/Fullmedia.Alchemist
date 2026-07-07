# Next Steps

For the full implementation scope, use `docs/DEVELOPMENT_CHECKLIST.md` as the master checklist.

For the current repo state, use `docs/CURRENT_STATUS.md`.

This file stays intentionally short and tracks the immediate next coding sequence only.

## Completed first coding pass

The initial MVP 1 application shell now exists:

1. PySide6 main window.
2. Visible app version.
3. Bottom footer/status bar.
4. Footer wired to internal tool registry hover metadata through tool-aware buttons.
5. Left profile/preset panel.
6. Center drag/drop queue panel.
7. Right inspector/preview placeholder panel.
8. Bottom progress/logs panel.
9. Default Alchemist Profiles and Output Presets load from JSON.
10. Basic validation pass for default JSON.

## Immediate next implementation task

Continue MVP 1 foundation work:

1. Add reusable drag/drop path field widget with browse button.
2. Add portable path resolver shell.
3. Add formal pydantic models for built-in Alchemist Profiles and Output Presets.
4. Replace lightweight validation with schema validation.
5. Add profile/preset store shell.
6. Add profile/preset duplicate shell.
7. Add Advanced JSON editor shell.
8. Add profile/preset import/export shell.
9. Add icon system placeholders/assets directory.
10. Add FFmpeg/ffprobe detection shell.

## After shell foundation is complete

1. Implement real profile/preset persistence.
2. Implement import/export validation.
3. Implement FFmpeg/ffprobe detection.
4. Wire Website Background conversion as first real workflow.
5. Add progress parsing and logs for real FFmpeg jobs.

## Known non-blocking decisions

- Installer design can wait.
- Full updater can wait.
- Full dependency-aware conversion graph can wait, but schema should not block it.
- Public release license audit can wait until before public binary distribution.
- Visual crop/pad editor can wait.
- Profile/preset diff viewer can wait.
- Advanced HDR tone-mapping can wait.

## Current conflict check

No blocking direction conflicts identified.

Clarification recorded:

Bundled FFmpeg means bundled into release packages so users do not need separate installation. The repo currently ignores raw `vendor/ffmpeg/*.exe` to avoid accidental large binary commits until a deliberate packaging decision is made.
