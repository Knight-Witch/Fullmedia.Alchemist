# Development Checklist

This checklist is the consolidated implementation source of truth for the planning conversation that defined Fullmedia Alchemist.

Use this as the master checklist before and during coding. When scope changes, update this file, `ROADMAP.md`, `docs/DECISIONS.md`, and `CHANGELOG.md` as needed.

## 0. Repository boundary and project hygiene

- [x] Project name is **Fullmedia Alchemist**.
- [x] GitHub repository is `Knight-Witch/Fullmedia.Alchemist`.
- [x] Visible app name is `Fullmedia Alchemist`.
- [x] Executable name target is `Fullmedia_Alchemist.exe`.
- [x] Python package name is `fullmedia_alchemist`.
- [x] Only edit the `Fullmedia.Alchemist` repository for this project.
- [x] Treat Witch Dock, Witch Tools, Witch Quickbar, Witch Dev, Blender tools, Heroforge scripts, and other repos as reference-only unless the user explicitly changes that rule.
- [x] Assets/icons may be copied from reference repos into Fullmedia Alchemist, but source repos must not be edited.
- [ ] Maintain `CHANGELOG.md` for every dev version bump.
- [ ] Maintain `docs/DECISIONS.md` for architectural decisions.
- [ ] Maintain `docs/DEV_LOG.md` for meaningful development sessions.
- [ ] Keep legacy scripts in a `legacy/` folder if/when copied into this repo.
- [ ] Do not wire production behavior directly to old standalone scripts; extract their logic into reusable modules.

## 1. Tech stack

- [x] Use Python.
- [x] Use PySide6 for the desktop UI.
- [x] Use FFmpeg/ffprobe as the media conversion/probing backend.
- [x] Use JSON for v0 Alchemist Profiles and Output Presets.
- [x] Use declarative JSON only for profile/preset code editing; do not allow arbitrary Python/JS/shell execution from imported presets.
- [x] Add `pydantic` as initial schema/validation candidate.
- [ ] Build formal schema/model classes for Alchemist Profiles.
- [ ] Build formal schema/model classes for Output Presets.
- [ ] Build formal schema/model classes for bundles/packs.
- [ ] Add validation tests for built-in JSON defaults.
- [ ] Add command-building tests for conversion modules.
- [ ] Add naming tests.
- [ ] Add import/export validation tests.

## 2. Release and packaging

- [x] First release target is portable ZIP.
- [x] Installer is optional later.
- [x] Users should only need to extract the ZIP and launch `Fullmedia_Alchemist.exe`.
- [x] Release package should bundle FFmpeg/ffprobe directly so users do not need a separate FFmpeg install.
- [x] Release package should include binaries, assets, default profiles, profile database/config/log/temp folders, and docs.
- [x] App should support portable-mode data beside the executable.
- [ ] Implement portable path resolver.
- [ ] Detect `user_data/` beside executable and use it for portable mode.
- [ ] Later support installed mode using `%LOCALAPPDATA%/Fullmedia Alchemist/`.
- [ ] Create real PyInstaller build config.
- [ ] Create real portable build script.
- [ ] Assemble release folder structure:
  - [ ] `Fullmedia_Alchemist.exe`
  - [ ] `bin/ffmpeg.exe`
  - [ ] `bin/ffprobe.exe`
  - [ ] `assets/icons/`
  - [ ] `assets/themes/`
  - [ ] `profiles/defaults/`
  - [ ] `user_data/config/`
  - [ ] `user_data/logs/`
  - [ ] `user_data/temp/`
  - [ ] `user_data/cache/`
  - [ ] `user_data/Converted_Originals/`
  - [ ] `docs/`
- [ ] Before public release, complete `THIRD_PARTY_LICENSES.md` for FFmpeg, PySide6/Qt, and copied icon assets.
- [ ] Decide deliberately whether FFmpeg binaries are committed in repo or injected during release packaging; current repo prevents accidental `vendor/ffmpeg/*.exe` commits.

## 3. Versioning and footer metadata

- [x] Dev version syntax is `Dev_vxxx.xxx.xxx_mm-dd-yy`.
- [x] Initial app version is `Dev_v000.001.000_07-06-26`.
- [x] Main app version must be visible in the UI at all times.
- [x] Footer/status bar must display main app version.
- [x] Footer/status bar must show internal tool/module identifier and version on hover.
- [x] Internal tool registry scaffold exists.
- [ ] Implement visible app version in the PySide6 UI.
- [ ] Implement bottom footer/status bar.
- [ ] Implement hover-to-footer metadata behavior.
- [ ] Register stable tool identifiers for major modules:
  - [x] `app_shell`
  - [x] `profile_validator`
  - [x] `conversion_engine`
  - [x] `gif_optimizer`
  - [x] `naming_engine`
  - [x] `website_background_profile`
  - [ ] `profile_store`
  - [ ] `profile_import_export`
  - [ ] `ffmpeg_runner`
  - [ ] `ffprobe_probe`
  - [ ] `video_ladder_encoder`
  - [ ] `png_series_processor`
  - [ ] `naming_preview`
  - [ ] `collision_handler`
  - [ ] `media_preview`
  - [ ] `progress_parser`
  - [ ] `path_resolver`
  - [ ] `portable_mode`
- [ ] Version bumps should update `version.py`, `CHANGELOG.md`, and relevant docs.

## 4. UI architecture

- [x] UI should be local desktop, not browser-based.
- [x] UI should be modular, collapsible, and customizable in spirit.
- [x] UX reference is Witch Dock / Witch Tools / Witch Quickbar / Witch Dev behavior, but those repos are reference-only.
- [x] UI should be icon-forward and visually clear, not dense text-heavy clutter.
- [x] Advanced settings should be collapsed by default.
- [x] Tooltips should explain icon-only controls.
- [ ] Implement main PySide6 window.
- [ ] Implement left panel for Alchemist Profiles and Output Presets.
- [ ] Implement center drag/drop queue panel.
- [ ] Implement right inspector/preview panel.
- [ ] Implement bottom progress/logs panel.
- [ ] Implement footer/status bar.
- [ ] Implement collapsible section widget.
- [ ] Implement icon button widget with tooltip + optional tool metadata ID.
- [ ] Implement reusable path field widget with browse button and drag/drop.
- [ ] Implement reusable file/folder drop zone widget.
- [ ] Implement media thumbnail/preview placeholder.
- [ ] Implement visual queue cards/rows.
- [ ] Implement warnings/errors display that is visible but not noisy.

## 5. Icon system and support/update buttons

- [x] Use universal icons for common actions where possible.
- [x] Avoid a shotgun blast of text across the UI.
- [x] Icons may be copied from existing Blender tools repo into this repo's assets, but only by copying; do not edit the source repo.
- [ ] Create `assets/icons/` structure.
- [ ] Copy/curate usable icons into Fullmedia Alchemist.
- [ ] Add icons for:
  - [ ] Save
  - [ ] Edit
  - [ ] Duplicate
  - [ ] Delete
  - [ ] Import/upload
  - [ ] Export/download
  - [ ] Settings gear
  - [ ] Browse/ellipsis
  - [ ] Drag/drop
  - [ ] Start
  - [ ] Pause
  - [ ] Stop
  - [ ] Open folder
  - [ ] Undo
  - [ ] Redo
  - [ ] Rollback
  - [ ] Validate
  - [ ] Warning
  - [ ] Success
  - [ ] Error
  - [ ] GitHub
  - [ ] Ko-fi
  - [ ] Patreon
  - [ ] Check updates
  - [ ] Install update
- [ ] Add icon-only buttons for:
  - [ ] Check for updates
  - [ ] Install downloaded update
  - [ ] Open GitHub repo
  - [ ] Open Ko-fi
  - [ ] Open Patreon
- [ ] Implement URL opening behavior for GitHub/Ko-fi/Patreon buttons.
- [ ] Implement updater UI shell even if full updater logic comes later.

## 6. Drag/drop requirements

- [x] Drag/drop should work for main file/folder queue input.
- [x] Drag/drop should work for source file/folder fields.
- [x] Drag/drop should work for output folder fields.
- [x] Drag/drop should work for completed-source/archive folder fields.
- [x] Drag/drop should work for profile/preset/pack import areas.
- [ ] Implement drag/drop for main queue.
- [ ] Implement drag/drop for source path widgets.
- [ ] Implement drag/drop for output path widgets.
- [ ] Implement drag/drop for archive/completed-source path widgets.
- [ ] Implement drag/drop for import widgets.
- [ ] Validate dropped item type and show readable errors when incompatible.

## 7. Data terminology and hierarchy

- [x] Alchemist Profile = parent workflow/mode for the tool.
- [x] Output Preset = reusable individual output recipe.
- [x] Profile Bundle = multiple Alchemist Profiles.
- [x] Output Preset Bundle = multiple Output Presets.
- [x] Full Alchemist Pack = Alchemist Profiles plus Output Presets.
- [x] Example Alchemist Profiles include Knight Witch Apparel, Heroforge, Instagram, Website Background, Etsy Media, Reddit GIF Pack.
- [x] Example Output Presets include GIF - Reddit 99MB, GIF - Discord 50MB, WebM - VP9 1080p, MP4 - H.264 fallback, Poster - WebP.
- [ ] Use this terminology consistently in UI text, docs, and code.
- [ ] Avoid calling Output Presets full profiles.
- [ ] Avoid calling Alchemist Profiles single file-output presets.

## 8. Alchemist Profile model

- [x] Alchemist Profiles should define workflow mode, input behavior, paths, naming, outputs, and source handling.
- [x] Alchemist Profiles should contain a list of Output Preset references and per-profile overrides.
- [x] Alchemist Profiles should allow locked/snapshot Output Preset versions.
- [x] Alchemist Profiles should allow linked Output Presets where explicitly chosen.
- [x] Built-in Website Background Alchemist Profile JSON seed exists.
- [ ] Implement Alchemist Profile model class.
- [ ] Implement Alchemist Profile validator.
- [ ] Implement loading built-in profiles from `profiles/defaults/alchemist_profiles/`.
- [ ] Implement user-created profile storage.
- [ ] Implement profile duplicate action.
- [ ] Implement profile delete/disable behavior.
- [ ] Implement profile search/filter.
- [ ] Implement profile editor UI.
- [ ] Implement profile Advanced JSON editor.
- [ ] Ensure bad profile JSON cannot break the tool.
- [ ] Add profile validation error popups.
- [ ] Add public-safe path variable support.
- [ ] Prevent public/default profiles from using Amanda-specific paths.

## 9. Output Preset model

- [x] Output Presets should define reusable file-output settings.
- [x] Output Presets can be added to multiple Alchemist Profiles.
- [x] Output Presets can be imported/exported independently.
- [x] Multiple Output Presets of the same output type must be allowed in one Alchemist Profile.
- [x] Built-in Website Background Output Presets exist for AV1 WebM ladder, VP9 WebM fallback ladder, H.264 MP4 fallback ladder, and WebP poster.
- [ ] Implement Output Preset model class.
- [ ] Implement Output Preset validator.
- [ ] Implement loading built-in presets from `profiles/defaults/output_presets/`.
- [ ] Implement user-created Output Preset storage.
- [ ] Implement Output Preset duplicate action.
- [ ] Implement Output Preset delete/disable behavior.
- [ ] Implement Output Preset search/filter.
- [ ] Implement Output Preset editor UI.
- [ ] Implement Output Preset Advanced JSON editor.
- [ ] Implement dropdown/selector to add Output Presets into an Alchemist Profile.
- [ ] Support linked versus copied/snapshot preset insertion.
- [ ] Detect profiles using older locked preset versions and offer update/keep behavior later.

## 10. Profile and preset version history

- [x] Profiles should track edit histories.
- [x] Output Presets should track edit histories.
- [x] Users should be able to roll back and roll forward a profile.
- [x] Users should be able to duplicate a profile from a prior version.
- [x] Each profile version should have a unique key/tag.
- [x] Each Output Preset version should have a unique key/tag.
- [ ] Design version snapshot database tables or storage files.
- [ ] Store profile snapshots on save.
- [ ] Store Output Preset snapshots on save.
- [ ] Implement profile rollback.
- [ ] Implement profile roll-forward.
- [ ] Implement Output Preset rollback.
- [ ] Implement Output Preset roll-forward.
- [ ] Implement duplicate from historical version.
- [ ] Show version history in editors.
- [ ] Optional later: version comparison/diff UI.

## 11. Editor undo/redo and field-level restore

- [x] Profile editor should support undo/redo while editing unsaved changes.
- [x] Output Preset editor should support undo/redo while editing unsaved changes.
- [x] Profile editor should have full restore/revert-to-last-saved behavior.
- [x] Output Preset editor should have full restore/revert-to-last-saved behavior.
- [x] Each field should have a small icon button to clear or revert that individual field's change.
- [ ] Implement editor state manager.
- [ ] Implement undo stack.
- [ ] Implement redo stack.
- [ ] Implement whole-profile restore.
- [ ] Implement whole-preset restore.
- [ ] Implement field-level revert.
- [ ] Implement field-level clear/reset.
- [ ] Ensure field-level controls stay visually subtle.

## 12. Profile import/export and packs

- [x] Support importing/exporting single Alchemist Profiles.
- [x] Support importing/exporting single Output Presets.
- [x] Support importing/exporting Profile Bundles.
- [x] Support importing/exporting Output Preset Bundles.
- [x] Support importing/exporting Full Alchemist Packs.
- [x] Support multi-profile batch import.
- [x] Support importing multiple profiles/presets from a ZIP.
- [x] Imports must validate before writing to local storage.
- [x] Invalid imports must fail safely with a popup and no tool breakage.
- [x] Import UI should show summary and conflicts.
- [ ] Implement `.fma-profile.json` import/export.
- [ ] Implement `.fma-output-preset.json` import/export.
- [ ] Implement `.fma-profile-bundle.zip` import/export.
- [ ] Implement `.fma-output-preset-bundle.zip` import/export.
- [ ] Implement `.fma-pack.zip` import/export.
- [ ] Implement manifest validation for ZIP packs.
- [ ] Implement dependency validation for profiles referencing presets.
- [ ] Implement conflict behavior:
  - [ ] Import as duplicate
  - [ ] Overwrite existing
  - [ ] Keep local/skip imported
  - [ ] Cancel
- [ ] Implement absolute-path warning/remapping on import.
- [ ] Implement readable validation failure popup.

## 13. Advanced JSON editor

- [x] New/edit profile UI should include a code input option.
- [x] Existing profile editor should include Advanced JSON editing.
- [x] Output Preset editor should include Advanced JSON editing.
- [x] Bad JSON must fail safely.
- [x] Arbitrary executable code must not be supported.
- [ ] Implement Advanced JSON tab for Alchemist Profiles.
- [ ] Implement Advanced JSON tab for Output Presets.
- [ ] Use the same validation pipeline for editor saves and imports.
- [ ] Highlight JSON parse errors.
- [ ] Show schema validation errors with field path and expected value type.
- [ ] Block save when invalid.
- [ ] Preserve last good profile/preset version if invalid edit is attempted.

## 14. Naming system

- [x] Auto naming should support cleaning messy names such as `Soldier copy copy copy`.
- [x] Auto naming should support folder-based naming for multi-file batches.
- [x] Manual override field should allow the user to type over the generated convention.
- [x] Whatever the user manually types should become the active convention for that batch/profile after validation.
- [x] Naming should support tokens.
- [x] Naming preview should show original name, cleaned name, pattern, and final output names.
- [x] Naming collision detection is required.
- [x] Naming history should help avoid repeated collisions.
- [ ] Implement name cleaner.
- [ ] Implement noise-word list.
- [ ] Implement rules such as remove after `copy`.
- [ ] Implement use-first-two-words-unless-second-is-noise behavior.
- [ ] Implement folder-based naming mode.
- [ ] Implement manual pattern override.
- [ ] Implement tokens:
  - [ ] `{base}`
  - [ ] `{original}`
  - [ ] `{source_stem}`
  - [ ] `{folder}`
  - [ ] `{profile}`
  - [ ] `{preset}`
  - [ ] `{date}`
  - [ ] `{time}`
  - [ ] `{##}`
  - [ ] `{###}`
  - [ ] `{height}`
  - [ ] `{width}`
  - [ ] `{codec_label}`
  - [ ] `{format}`
  - [ ] `{extension}`
  - [ ] `{output_suffix}`
- [ ] Implement live naming preview.
- [ ] Implement collision warning.
- [ ] Implement add-sequence-token suggestion.
- [ ] Implement overwrite/skip/cancel options.
- [ ] Implement global/per-profile/per-output-folder naming history options.

## 15. Conversion engine architecture

- [x] Engine should be independent of UI.
- [x] Engine should use FFmpeg/ffprobe.
- [x] Engine should support files, folders, archives, videos, GIFs, PNG series, still images, and output sets over time.
- [x] Engine should preserve highest practical apparent visual fidelity under selected constraints.
- [x] Core priorities are resolution, color fidelity, dimensions/aspect ratio, and framerate/source timing.
- [x] Engine should support multiple outputs from the same source.
- [x] Engine should support multiple outputs of the same file type.
- [x] Engine should eventually support dependency-aware output graphs and intermediates when useful.
- [ ] Implement media probe wrapper around ffprobe.
- [ ] Implement FFmpeg executable/path resolver.
- [ ] Implement FFmpeg encoder availability checks.
- [ ] Implement FFmpeg command builder.
- [ ] Implement FFmpeg runner.
- [ ] Implement machine-readable progress parser.
- [ ] Implement job queue model.
- [ ] Implement conversion result model.
- [ ] Implement temp file manager.
- [ ] Implement output dependency graph planner.
- [ ] Implement optional intermediate output handling.
- [ ] Implement cleanup rules for temp/intermediate files.

## 16. Quality and size-targeting behavior

- [x] Use “visually lossless” as shorthand for fidelity-first practical output under format constraints.
- [x] Do not re-litigate GIF limitations in app/user docs unless relevant to behavior.
- [x] For hard file-size caps, generate temporary outputs, measure size, and revise until the closest/highest-quality acceptable candidate under the cap is found.
- [x] If cap cannot be met within minimum quality boundaries, fail with a clear explanation.
- [x] Do not silently create potato-quality garbage.
- [ ] Implement quality policy model.
- [ ] Implement candidate-encode loop for size-targeted formats.
- [ ] Implement binary/candidate search over dimensions.
- [ ] Preserve FPS by default where profile specifies it.
- [ ] Allow FPS reduction only when profile/preset permits it.
- [ ] Track current candidate size/settings in progress UI.
- [ ] Track best acceptable candidate so far.
- [ ] Report best failed candidate and required compromise when target cannot be met.

## 17. GIF workflows

- [x] GIF workflows should support 99/100 MB targets, 49/50 MB targets, and arbitrary caps.
- [x] GIF optimizer should use temporary test outputs.
- [x] GIF optimizer should use palette generation/palette use where appropriate.
- [x] GIF optimizer should preserve apparent color/fidelity as much as possible under cap.
- [x] GIF optimizer should support multiple GIF presets from one source, such as 99 MB and 50 MB.
- [ ] Implement GIF optimizer module.
- [ ] Implement palette generation.
- [ ] Implement palette use.
- [ ] Implement long-edge/even-dimension scaling strategies.
- [ ] Implement size cap search.
- [ ] Implement min/max dimension settings.
- [ ] Implement dimension step setting.
- [ ] Implement preserve/force FPS setting.
- [ ] Implement loop replay setting.
- [ ] Implement no-sound behavior for GIF source conversions where relevant.

## 18. Video/WebM/MP4 workflows

- [x] Website background workflow should generate multi-size AV1 WebM.
- [x] Website background workflow should generate VP9 WebM fallback.
- [x] Website background workflow should generate H.264 MP4 fallback.
- [x] Website background workflow should generate WebP poster.
- [x] Website background workflow should skip HDR/10-bit-looking sources by default.
- [x] Website background workflow should preserve source color metadata when present.
- [x] Website background workflow should use bt709/tv fallback metadata for SDR web video.
- [x] Website background workflow should remove audio by default.
- [x] Website background workflow should not upscale.
- [x] Website background workflow should use Lanczos scaling.
- [ ] Implement AV1 WebM encoder module.
- [ ] Implement VP9 WebM encoder module.
- [ ] Implement H.264 MP4 encoder module.
- [ ] Implement WebP poster module.
- [ ] Implement HDR/10-bit detector.
- [ ] Implement color metadata extraction.
- [ ] Implement color flag builder.
- [ ] Implement downscale-only scaling helper.
- [ ] Implement poster timestamp fallback.
- [ ] Implement required encoder checks for `libsvtav1`, `libvpx-vp9`, and `libx264`.

## 19. PNG series workflows

- [x] App should eventually support PNG series conversion based on existing script behavior.
- [x] PNG series should natural-sort frames.
- [x] PNG series should stage frames to clean sequential names.
- [x] PNG series should support GIF, WebP, WebM, MP4, and Reddit/size-capped GIF outputs.
- [x] PNG series should support folder and archive inputs.
- [ ] Implement PNG series detector.
- [ ] Implement natural sort.
- [ ] Implement staging to `frame_%06d.png`.
- [ ] Implement archive extraction for `.zip`/`.cbz` if enabled.
- [ ] Implement generated outputs through Output Presets.
- [ ] Implement mark-done/rename-done option if needed.
- [ ] Implement source archive/move behavior for folders and archives.

## 20. Resize/crop/ratio behavior

- [x] Profiles should support preserving original size.
- [x] Profiles should support scale-to-long-edge.
- [x] Profiles should support exact output resolution.
- [x] Profiles should support aspect-ratio crop or pad.
- [x] Profiles should support square to 16:9 cases and exact resize cases like 2500x2500 to 400x400.
- [x] Profiles should support crop anchor/position.
- [ ] Implement resize settings model.
- [ ] Implement crop settings model.
- [ ] Implement pad settings model.
- [ ] Implement crop anchor choices:
  - [ ] center
  - [ ] top
  - [ ] bottom
  - [ ] left
  - [ ] right
  - [ ] custom X/Y
- [ ] Implement preview of crop/pad behavior later.

## 21. Audio and loop behavior

- [x] Profiles/Output Presets should support sound/no-sound behavior.
- [x] Profiles/Output Presets should support loop replay behavior.
- [x] Website background removes audio by default.
- [ ] Implement audio mode setting:
  - [ ] preserve
  - [ ] remove
  - [ ] convert later if needed
- [ ] Implement loop mode setting:
  - [ ] no loop
  - [ ] loop forever
  - [ ] loop N times where format supports it
- [ ] Ensure unsupported audio/loop settings validate cleanly per output format.

## 22. Source handling and archive behavior

- [x] Source file/folder should move only after successful conversion when configured.
- [x] If conversion fails, source should remain in place.
- [x] Users can choose what happens to source files/folders after completion.
- [x] If move/archive is enabled but no destination is specified, default to app-created `Converted_Originals` so files are retrievable.
- [ ] Implement source handling modes:
  - [ ] leave in place
  - [ ] move after success
  - [ ] copy after success
  - [ ] rename as done
  - [ ] archive to app `Converted_Originals`
  - [ ] archive to output-folder `Converted_Originals`
  - [ ] archive to custom folder
- [ ] Implement conflict behavior for archive destination filename collisions.
- [ ] Implement source folder handling separately from single-file handling.
- [ ] Ensure failed conversions never move/delete source data.

## 23. Progress, ETA, logs, and failure display

- [x] UI needs visual progress bar with percent.
- [x] UI should show time estimate.
- [x] UI should show expected finish timestamp.
- [x] UI should show current operation and current file.
- [x] UI should show logs in a collapsible bottom panel.
- [x] Optimizer jobs should show current test candidate and best candidate so far where possible.
- [ ] Implement progress model.
- [ ] Implement elapsed time.
- [ ] Implement ETA estimate.
- [ ] Implement expected finish timestamp.
- [ ] Implement per-job logs.
- [ ] Implement persistent log files.
- [ ] Implement UI log filtering/collapsing.
- [ ] Implement readable failure cards/popups.
- [ ] Implement failed job continuation behavior for batch queues.

## 24. Website Background dev profile

- [x] Latest website-background conversion script uploaded and documented.
- [x] Default Website Background Alchemist Profile JSON exists.
- [x] Default AV1 WebM Output Preset JSON exists.
- [x] Default VP9 WebM fallback Output Preset JSON exists.
- [x] Default H.264 MP4 fallback Output Preset JSON exists.
- [x] Default WebP poster Output Preset JSON exists.
- [ ] Validate seeded Website Background JSON against model classes.
- [ ] Load seeded Website Background profile in UI.
- [ ] Display linked Output Presets in profile editor.
- [ ] Wire actual conversion behavior.
- [ ] Test with local MP4 source.
- [ ] Confirm source moves only after full success.
- [ ] Confirm failed source remains in place.

## 25. Public profile/preset sharing

- [x] Users should be able to share Profile Bundles, Output Preset Bundles, and Full Alchemist Packs.
- [x] User may create a Heroforge server bundle later.
- [x] Shared public/default profiles should not inherit Amanda-specific paths.
- [ ] Implement path-variable remapping on import.
- [ ] Implement profile/preset dependency summary.
- [ ] Implement export selected profiles.
- [ ] Implement export selected Output Presets.
- [ ] Implement export all user profiles/presets.
- [ ] Implement full pack export with dependencies included.
- [ ] Implement pack metadata display.
- [ ] Implement import preview before committing changes.

## 26. Update system

- [x] UI should include check-for-updates icon button.
- [x] UI should include install-downloaded-update icon button.
- [x] GitHub release distribution is planned; no MS Store/app store.
- [ ] Implement GitHub repo link button.
- [ ] Implement GitHub Releases check later.
- [ ] Compare current app version against latest release later.
- [ ] Download release package later.
- [ ] Decide updater helper behavior later.
- [ ] Implement safe update flow for portable app later.

## 27. Safety and validation

- [x] Profile/preset JSON should not be executable.
- [x] Bad profile/preset code should fail with popup.
- [x] Failed imports/saves should not corrupt the tool.
- [x] Imported profiles should be validated before save.
- [x] Imported bundles should be validated before save.
- [x] Source files should not move/delete on failure.
- [ ] Add schema validation for all defaults.
- [ ] Add destructive-path validation.
- [ ] Add output path equals source path warning/block when unsafe.
- [ ] Add unknown-field handling policy.
- [ ] Add unsupported schema migration/failure behavior.
- [ ] Add readable error messages with field path, actual value, and expected value.

## 28. MVP 1 implementation sequence

- [ ] Create PySide6 app shell.
- [ ] Display app name and version.
- [ ] Add footer/status bar.
- [ ] Wire footer/status bar to tool registry.
- [ ] Add left Alchemist Profile / Output Preset panel.
- [ ] Add center drag/drop queue panel.
- [ ] Add right inspector/preview placeholder.
- [ ] Add bottom logs/progress panel.
- [ ] Load built-in JSON profiles/presets.
- [ ] Validate built-in JSON profiles/presets.
- [ ] Add icon system placeholders.
- [ ] Add profile/preset duplicate shell.
- [ ] Add Advanced JSON editor shell.
- [ ] Add import/export shell.
- [ ] Add portable path resolver shell.

## 29. MVP 2 implementation sequence

- [ ] Implement profile/preset store.
- [ ] Implement profile/preset validation fully enough for built-ins.
- [ ] Implement FFmpeg/ffprobe path detection.
- [ ] Implement media probe.
- [ ] Implement Website Background conversion workflow.
- [ ] Implement progress parsing.
- [ ] Implement logs.
- [ ] Implement source move-after-success.
- [ ] Test Website Background workflow end-to-end.

## 30. MVP 3 implementation sequence

- [ ] Implement GIF optimizer.
- [ ] Implement PNG series processor.
- [ ] Implement size-capped GIF presets.
- [ ] Implement multiple GIF outputs from same source.
- [ ] Implement naming engine and preview.
- [ ] Implement source archive behavior.

## 31. MVP 4 implementation sequence

- [ ] Implement profile version history.
- [ ] Implement Output Preset version history.
- [ ] Implement rollback/roll-forward.
- [ ] Implement bundle/pack import/export.
- [ ] Implement linked/copy preset behavior.

## 32. MVP 5 implementation sequence

- [ ] Implement public-release polish.
- [ ] Implement updater/check release flow.
- [ ] Complete license audit.
- [ ] Build portable ZIP.
- [ ] Add public user docs.
- [ ] Prepare GitHub release.

## 33. Items intentionally deferred but planned

- [ ] Installer.
- [ ] Full self-updater helper.
- [ ] Visual crop/pad editor.
- [ ] Profile/preset diff viewer.
- [ ] Public preset discovery/marketplace.
- [ ] Advanced tone-mapping for HDR sources.
- [ ] Audio conversion/normalization beyond preserve/remove.

## 34. Current conflict check

- [x] No conflict found between current conversation requirements and the current repository direction.
- [x] Only notable implementation caveat: user wants FFmpeg bundled for users; current repo ignores raw `vendor/ffmpeg/*.exe` to avoid accidental binary bloat, while release packages still need bundled FFmpeg/ffprobe.
