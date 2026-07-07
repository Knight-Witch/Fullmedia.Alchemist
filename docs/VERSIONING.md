# Versioning and Footer Metadata

## Main app version

The app version must be visible in the UI at all times.

Development version syntax:

```text
Dev_vxxx.xxx.xxx_mm-dd-yy
```

Example:

```text
Dev_v000.001.000_07-06-26
```

Public release versions can later use normal release labels:

```text
v0.1.0-alpha
v0.2.0-beta
v1.0.0
```

## UI locations

The app version may appear in:

- Window title.
- Top-right app header.
- Footer/status bar right side.

Example:

```text
Fullmedia Alchemist — Dev_v000.001.000_07-06-26
```

## Footer/status bar

The bottom footer should display subtle, useful development information.

Default state:

```text
Ready     Fullmedia Alchemist • Dev_v000.001.000_07-06-26
```

Hovering over a registered tool/function should display internal tool metadata:

```text
GIF Optimizer • gif_optimizer • Dev_v000.002.004_07-06-26 • Binary-search size targeting
```

## Internal tool metadata

Major modules/tools should have stable identifiers.

Recommended identifiers:

```text
app_shell
profile_store
profile_validator
profile_import_export
conversion_engine
ffmpeg_runner
ffprobe_probe
gif_optimizer
video_ladder_encoder
website_background_profile
png_series_processor
naming_engine
naming_preview
collision_handler
media_preview
progress_parser
path_resolver
portable_mode
```

## Metadata shape

Each internal tool/module can expose:

```python
TOOL_ID = "gif_optimizer"
TOOL_NAME = "GIF Optimizer"
TOOL_VERSION = "Dev_v000.001.000_07-06-26"
TOOL_DESCRIPTION = "Size-targeted GIF optimization."
```

Or register equivalent metadata in a central registry.

## Version registry

Recommended files:

```text
src/fullmedia_alchemist/version.py
src/fullmedia_alchemist/core/tool_registry.py
```

`version.py` should own:

```python
APP_NAME = "Fullmedia Alchemist"
APP_VERSION = "Dev_v000.001.000_07-06-26"
BUILD_DATE = "07-06-26"
```

## Changelog requirement

Every dev version bump should have a `CHANGELOG.md` entry.

Every meaningful architectural decision should be added to `docs/DECISIONS.md`.

Every dev work session should add/update `docs/DEV_LOG.md` when appropriate.
