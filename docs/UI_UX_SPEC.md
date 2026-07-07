# UI / UX Specification

## UX reference

The app should use a modular, collapsible, customizable desktop-workbench style inspired by previous Witch Dock, Witch Tools, Witch Quickbar, and Witch Dev projects.

Those repositories are reference-only. They must not be edited for this project.

## UI personality

Fullmedia Alchemist should not be a dense wall of text or a console wrapped in a window.

The UI should be:

- Modular.
- Collapsible.
- Icon-forward.
- Visually clear.
- Friendly to ADHD/autism usage patterns.
- Strong on visual hierarchy.
- Conservative with dense text.
- Tooltips available where icons need explanation.
- Advanced settings collapsed by default.

## Main window layout

### Left panel: Profiles and presets

Contains:

- Alchemist Profiles.
- Output Presets.
- Packs/import/export controls.
- Search/filter.
- Duplicate/edit/delete/import/export actions.

### Center panel: Drop zone and queue

Contains:

- Large drag/drop target.
- Add file button.
- Add folder button.
- Queue list.
- Current status per queued item.
- Start/pause/stop controls.

### Right panel: Inspector and preview

Contains selected-job information:

- Thumbnail or playable preview.
- Source metadata.
- Resolution.
- Duration.
- FPS.
- Frame count when available.
- Audio presence.
- Output preview names.
- Destination paths.
- Warnings.

### Bottom panel: Progress and logs

Contains:

- Current operation.
- Current file.
- Current output/test candidate.
- Progress bar.
- Percent.
- Elapsed time.
- ETA.
- Expected finish timestamp.
- Collapsible log stream.
- Failure details.

### Footer/status bar

Always present and subtle.

Default state:

```text
Ready     Fullmedia Alchemist • Dev_v000.001.000_07-06-26
```

On hover over a registered tool/function:

```text
GIF Optimizer • gif_optimizer • Dev_v000.002.004_07-06-26 • Binary-search size targeting
```

## Profile editor layout

The Alchemist Profile editor should use collapsible sections:

- General.
- Input.
- Output Presets.
- Paths.
- Naming.
- Resize / Crop.
- Audio / Loop.
- Source Handling.
- Advanced Settings.
- Advanced JSON.
- Version History.

## Output Preset editor layout

The Output Preset editor should use collapsible sections:

- General.
- Format.
- Codec.
- Size Cap.
- Quality Policy.
- Resize / Crop.
- FPS / Timing.
- Audio / Loop.
- Naming Suffix / Pattern Fragment.
- Advanced JSON.
- Version History.

## Icons

Use universal icons where possible:

- Save.
- Edit.
- Duplicate.
- Delete.
- Import/upload.
- Export/download.
- Settings gear.
- Browse/ellipsis.
- Drag/drop.
- Start.
- Pause.
- Stop.
- Open folder.
- Undo.
- Redo.
- Rollback.
- Validate.
- Warning.
- Success.
- Error.
- GitHub.
- Ko-fi.
- Patreon.
- Check updates.
- Install update.

Text labels should be used where they improve clarity, but the app should not become a shotgun blast of text.

## Drag/drop requirements

Drag/drop should work for:

- Main queue input.
- Source file fields.
- Source folder fields.
- Output folder fields.
- Completed-source/archive folder fields.
- Profile import areas.
- Pack import areas.

## Profile editing ergonomics

Profile and Output Preset editors should include:

- Undo.
- Redo.
- Save.
- Save As / Duplicate.
- Cancel.
- Restore whole profile/preset to last saved state.
- Field-level revert button.
- Field-level clear/reset button.

Field-level controls should be small icon buttons, not large text-heavy UI.

## Update/support buttons

The UI should include small icon-only buttons for:

- Check for updates.
- Install downloaded update.
- Open GitHub repo.
- Open Ko-fi.
- Open Patreon.

The full updater can be implemented after MVP 1, but the UI slots should be reserved early.
