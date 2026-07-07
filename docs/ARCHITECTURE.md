# Architecture

## Principle

Do not wrap old scripts directly in a GUI. Extract their useful logic into reusable modules, then build a PySide6 interface around those modules.

The app should be structured as a reusable conversion engine plus a profile/preset-driven UI.

## Primary layers

### UI layer

PySide6 desktop UI.

Responsibilities:

- Main window and layout.
- Modular/collapsible panels.
- Icon buttons and tooltips.
- Drag/drop handling.
- Profile and Output Preset editing.
- Queue display.
- Preview/inspector display.
- Progress and logs.
- Footer/status bar version metadata display.

The UI should not own conversion logic.

### Profile and preset layer

Responsibilities:

- Alchemist Profile model.
- Output Preset model.
- Profile Bundle model.
- Output Preset Bundle model.
- Full Alchemist Pack model.
- JSON validation.
- Import/export.
- Version history.
- Duplicate/rollback/roll-forward.
- Linked versus copied Output Preset behavior.

### Conversion engine layer

Responsibilities:

- Build conversion plans.
- Probe media.
- Build FFmpeg commands.
- Run FFmpeg safely.
- Parse progress.
- Manage temporary files.
- Run size-targeting candidate encodes.
- Run dependency-aware output pipelines.
- Move/copy/archive originals after successful conversion only.

### Storage layer

Responsibilities:

- Portable versus installed-mode path resolution.
- Config storage.
- Profile/preset database.
- Profile/preset version snapshots.
- Logs.
- Temp/cache directories.
- Default archive folder, such as `Converted_Originals`.

## Recommended repository structure

```text
Fullmedia.Alchemist/
  README.md
  ROADMAP.md
  CHANGELOG.md
  THIRD_PARTY_LICENSES.md
  pyproject.toml

  docs/
    PROJECT_BRIEF.md
    ARCHITECTURE.md
    UI_UX_SPEC.md
    PROFILE_SCHEMA.md
    OUTPUT_PRESETS.md
    PROFILE_IMPORT_EXPORT.md
    NAMING_RULES.md
    CONVERSION_ENGINE.md
    BUILD_AND_RELEASE.md
    VERSIONING.md
    REFERENCE_ONLY_REPOS.md
    DECISIONS.md
    DEV_LOG.md

  src/
    fullmedia_alchemist/
      __init__.py
      main.py
      version.py

      core/
        conversion_engine.py
        ffmpeg_runner.py
        ffprobe_runner.py
        progress_parser.py
        media_probe.py
        job_queue.py
        job_model.py
        temp_manager.py

      optimization/
        gif_optimizer.py
        size_targeting.py
        quality_policy.py
        test_encode.py

      profiles/
        alchemist_profile.py
        output_preset.py
        profile_store.py
        profile_validator.py
        profile_history.py
        default_profiles.py
        schema.py

      naming/
        name_cleaner.py
        naming_rules.py
        naming_tokens.py
        naming_preview.py
        collision_handler.py
        naming_history.py

      ui/
        main_window.py
        panels/
        widgets/

      storage/
        path_resolver.py
        app_config.py
        database.py

      assets/
        icons/
        themes/

  scripts/
    dev_run.bat
    build_portable.bat
    build_portable.py
    clean_build.bat

  vendor/
    ffmpeg/
      ffmpeg.exe
      ffprobe.exe

  tests/
```

## Conversion planning model

The app should eventually use a conversion graph, not a flat list of isolated commands.

Example:

```text
PNG sequence
  -> staged frame sequence
  -> intermediate MP4 if useful
  -> final WebM output
  -> final GIF 99MB output
  -> final GIF 49MB output
```

Not every workflow needs an intermediate, but the architecture should support one output depending on another when it improves quality, speed, or consistency.

## Safety rules

- Profiles and Output Presets are declarative JSON, not executable scripts.
- Imported JSON must validate before it can be saved.
- Failed imports must not mutate the database.
- Source files should not be moved until required outputs succeed.
- Failed conversions should leave source files in place.
- Temp files should be cleaned when safe, but logs should preserve enough information for debugging.
- Public/default profiles must not contain Amanda-specific local paths.

## Active repository boundary

Only `Fullmedia.Alchemist` is edited for this project.

Other repositories may be used as visual/UX/assets reference only and must not be modified for this project.
