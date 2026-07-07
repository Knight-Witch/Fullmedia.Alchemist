# Decision Log

## Dev_v000.001.000_07-06-26

### Project name

Decision: app name is **Fullmedia Alchemist**.

Repo: `Fullmedia.Alchemist`.

Executable: `Fullmedia_Alchemist.exe`.

### Active repo boundary

Decision: only `Fullmedia.Alchemist` is edited for this project.

Other repos are reference-only and may supply UX ideas or copied assets, but must not be modified.

### App platform

Decision: local Windows desktop app.

No browser-based app, no web-hosted conversion tool, no app-store/MS Store dependency.

### UI framework

Decision: Python + PySide6.

Reason: local desktop UI, good fit for modular/collapsible panels, existing Python conversion-script base.

### Conversion backend

Decision: FFmpeg/ffprobe backend.

Reason: required for high-quality video/image/audio probing and conversion workflows.

### FFmpeg release handling

Decision: bundle FFmpeg/ffprobe directly with portable releases.

Reason: user should not need to install FFmpeg manually.

### Release mode

Decision: portable ZIP first; installer optional later.

Reason: easiest GitHub release path and best fit for a local utility.

### Profile format

Decision: JSON for v0 Alchemist Profiles and Output Presets.

Reason: strict, easy to validate, safer for import/export than executable code.

### Profile code editor

Decision: include an Advanced JSON editor for profiles/presets, but do not allow arbitrary executable code.

All JSON must validate before save/import.

### Main terminology

Decision:

- Alchemist Profile: parent workflow/mode.
- Output Preset: reusable file-output recipe.
- Profile Bundle: multiple Alchemist Profiles.
- Output Preset Bundle: multiple Output Presets.
- Full Alchemist Pack: profiles plus presets.

### UI style

Decision: modular, collapsible, icon-forward desktop workbench.

The UI should not be text-dense.

### Version visibility

Decision: app version must always be visible. Footer/status bar must show internal tool/module version metadata on hover.

Dev syntax:

```text
Dev_vxxx.xxx.xxx_mm-dd-yy
```

### First real workflow

Decision: Website Background conversion should be the first real conversion workflow wired after the UI shell.

It should create AV1 WebM, VP9 WebM fallback, H.264 MP4 fallback, and WebP poster outputs from MP4 sources.
