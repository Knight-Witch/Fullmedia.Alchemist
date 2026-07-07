# Alchemist Profile Schema

## Format

Profiles use JSON for v0.

Profile JSON is declarative configuration only. It must not contain executable Python, JavaScript, shell commands, or arbitrary scripts.

All profile JSON must validate against the app schema before it can be saved, imported, duplicated, or applied.

## Meaning

An **Alchemist Profile** is the parent workflow/mode for the tool.

Examples:

- Knight Witch Apparel.
- Heroforge.
- Instagram.
- Website Background.
- Etsy Media.
- Reddit GIF Pack.

An Alchemist Profile is not one output file type. It defines how a batch/conversion workflow behaves and which Output Presets are included.

## Required conceptual fields

```json
{
  "schema_version": "1.0",
  "kind": "alchemist_profile",
  "profile_id": "website_background",
  "profile_name": "Website Background",
  "profile_version_id": "apv_000001_07-06-26_1900",
  "description": "Creates website background video output sets.",
  "input": {},
  "paths": {},
  "naming": {},
  "outputs": [],
  "source_handling": {},
  "metadata": {}
}
```

## Input section

Defines accepted sources.

Possible fields:

```json
{
  "accepted_extensions": [".mp4", ".gif", ".png", ".zip", ".cbz"],
  "accept_files": true,
  "accept_folders": true,
  "accept_archives": true,
  "recursive": false,
  "allow_drag_drop": true
}
```

## Paths section

Defines default paths and path behavior.

Public/default profiles should use placeholders/variables, not Amanda-specific paths.

Possible variables:

```text
{user_home}
{downloads}
{desktop}
{documents}
{app_dir}
{user_data}
{profile_output}
{source_parent}
{source_stem}
```

## Outputs section

An Alchemist Profile contains a list of Output Preset references and optional per-profile overrides.

```json
{
  "outputs": [
    {
      "output_preset_id": "gif_reddit_99mb",
      "preset_version_mode": "locked",
      "preset_version_id": "opv_000001_07-06-26_1900",
      "enabled": true,
      "overrides": {
        "name_suffix": "_REDDIT_99MB"
      }
    }
  ]
}
```

## Linked versus copied presets

When an Output Preset is added to an Alchemist Profile, the app should support two modes.

### Linked

The profile references the Output Preset. The app can detect when a newer preset version exists and offer to update.

### Copied/snapshot

The profile receives an internal copy of the preset settings. Future changes to the original Output Preset do not affect the profile.

Default should be conservative: lock to a specific preset version unless the user chooses live/latest behavior.

## Version history

Each saved profile edit should create a version snapshot.

Useful fields:

```json
{
  "profile_id": "website_background",
  "profile_version_id": "apv_000006_07-06-26_1942",
  "created_at": "2026-07-06T19:42:00-07:00",
  "created_by_app_version": "Dev_v000.001.000_07-06-26",
  "change_note": "Adjusted VP9 fallback ladder.",
  "snapshot": {}
}
```

The app should support:

- Rollback.
- Roll-forward.
- Duplicate from version.
- Export version.
- Compare later if implemented.

## Editing behavior

The editor should support:

- Undo.
- Redo.
- Restore whole profile to last saved state.
- Field-level revert.
- Field-level clear/reset.
- Validation before save.
- Validation before import.

## Validation rules

Reject profiles when:

- JSON is malformed.
- Required fields are missing.
- `schema_version` is unsupported and no migration exists.
- `kind` is not `alchemist_profile`.
- Referenced Output Presets are missing and not embedded in the import package.
- Output references create unavoidable filename collisions.
- Path behavior is unsafe.
- A destructive source action is configured without safe fallback behavior.
- Unknown fields are present in strict mode.
- Executable/script content is detected.

Invalid profiles must fail safely with a readable popup and no database mutation.
