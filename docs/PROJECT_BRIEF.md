# Project Brief

## Purpose

Fullmedia Alchemist is a local Windows desktop app for repeatable, high-fidelity media conversion workflows.

It replaces a collection of one-off Python and BAT conversion scripts with a modular, profile-driven desktop tool that can batch-convert files, folders, PNG sequences, GIFs, videos, and archives into multiple target formats and size/quality variants.

The tool is intended to be useful for both private Knight Witch workflows and eventual public GitHub release.

## Non-negotiable direction

- Local Windows desktop app.
- No browser-based UI.
- No cloud conversion.
- No app-store dependency.
- First release as a portable ZIP.
- App launch should be simple: run `Fullmedia_Alchemist.exe`.
- FFmpeg/ffprobe should be bundled with the release package.
- Profile and preset data should use JSON in v0.
- Invalid profile JSON must never break the app.
- Other repos are reference/assets-only; only this repo is edited for this project.

## Main user workflow

1. Launch `Fullmedia_Alchemist.exe`.
2. Select an Alchemist Profile, such as Knight Witch Apparel, Heroforge, Website Background, or Reddit GIF Pack.
3. Drag/drop a file, folder, or archive into the queue, or use browse buttons.
4. Review generated output names, selected Output Presets, preview/metadata, and destination folders.
5. Press Start.
6. Watch progress, ETA, expected finish time, and logs.
7. App writes outputs and moves originals only after successful conversion if that option is enabled.

## Quality philosophy

The tool should prioritize the final visual result.

Important priorities:

- Resolution.
- Color fidelity.
- Correct dimensions/aspect ratio.
- Framerate/source timing.
- Avoiding potato-quality garbage.

When a hard file-size cap exists, the engine should create temporary candidate outputs, measure file size, and converge on the highest-quality candidate under the cap while respecting minimum quality boundaries.

If the target cannot be met within those boundaries, the app should fail clearly and explain which limits prevented success.

## Terminology

### Alchemist Profile

The parent mode/workflow for the tool. Example: Knight Witch Apparel, Heroforge, Instagram, Website Background.

### Output Preset

A reusable output recipe for one file-output target. Example: GIF - Reddit 99MB, GIF - Discord 50MB, WebM - VP9 1080p.

### Profile Bundle

A multi-profile export/import package containing multiple Alchemist Profiles.

### Output Preset Bundle

A multi-preset export/import package containing Output Presets that are added to the user's available Output Preset list.

### Full Alchemist Pack

A combined bundle containing Alchemist Profiles plus the Output Presets they use.

## First dev profile

The first real workflow to wire into the app should be the Website Background conversion profile based on the current standalone script.

It should convert MP4 website-background sources into:

- AV1 WebM ladder.
- VP9 WebM fallback ladder.
- H.264 MP4 fallback ladder.
- WebP poster image.

It should preserve SDR color metadata when present, skip HDR/10-bit-looking sources by default, avoid upscaling, remove audio, and move source files only after successful conversion.
