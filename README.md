# Fullmedia Alchemist

Fullmedia Alchemist is a local Windows desktop media conversion workbench for converting images, PNG sequences, GIFs, videos, and folders/archives into platform-ready output sets.

The app is designed around saved **Alchemist Profiles** and reusable **Output Presets** so users can build repeatable workflows such as website background conversion, Heroforge media conversion, Reddit GIF packs, Etsy/product media, Instagram media, and other batch conversion pipelines.

## Core direction

- Local Windows desktop app.
- No browser-hosted workflow.
- Portable ZIP release first; installer optional later.
- Main executable: `Fullmedia_Alchemist.exe`.
- Python + PySide6 UI.
- FFmpeg/ffprobe backend, bundled directly with the app release.
- JSON profile and preset format for v0.
- Modular, collapsible, icon-forward UI.
- Drag/drop support for files, folders, source paths, output paths, archive paths, profile imports, and queue input.
- Visual preview/inspector for selected jobs.
- Progress bar with percent, ETA, and expected finish timestamp.
- Footer/status bar with visible app version and internal tool/module hover versioning.

## Key concepts

### Alchemist Profile

A parent workflow mode for the tool. Example Alchemist Profiles could include:

- Knight Witch Apparel
- Heroforge
- Instagram
- Website Background
- Etsy Media
- Reddit GIF Pack

An Alchemist Profile defines input behavior, batch behavior, naming behavior, output folder behavior, source handling, and the list of Output Presets to run.

### Output Preset

A reusable file-output recipe. Examples:

- GIF - Reddit 99MB
- GIF - Discord 50MB
- WebM - VP9 1080p
- MP4 - H.264 Fallback 720p
- Poster - WebP 85

Output Presets can be added to multiple Alchemist Profiles.

### Profile Bundle

A bundle containing multiple Alchemist Profiles.

### Output Preset Bundle

A bundle containing multiple Output Presets that are added to the user's available Output Preset list.

### Full Alchemist Pack

A bundle containing Alchemist Profiles plus the Output Presets they depend on.

## Release model

The first release target is a portable ZIP:

```text
Fullmedia_Alchemist_Portable_v0.1.0/
  Fullmedia_Alchemist.exe
  bin/
    ffmpeg.exe
    ffprobe.exe
  assets/
  profiles/
  user_data/
    config/
    logs/
    temp/
    cache/
    Converted_Originals/
  docs/
```

Users should only need to extract the ZIP and launch `Fullmedia_Alchemist.exe`.

## Development status

Initial planning/scaffold phase. See `ROADMAP.md`, `CHANGELOG.md`, and the `docs/` directory.
