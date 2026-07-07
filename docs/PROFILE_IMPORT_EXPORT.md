# Profile Import / Export

## Supported export/import concepts

### Single Alchemist Profile

One parent workflow profile.

Suggested extension:

```text
.fma-profile.json
```

### Single Output Preset

One reusable output recipe.

Suggested extension:

```text
.fma-output-preset.json
```

### Profile Bundle

Multiple Alchemist Profiles.

Suggested extension:

```text
.fma-profile-bundle.zip
```

### Output Preset Bundle

Multiple Output Presets not necessarily tied to any Alchemist Profile.

Suggested extension:

```text
.fma-output-preset-bundle.zip
```

### Full Alchemist Pack

Alchemist Profiles plus the Output Presets they depend on.

Suggested extension:

```text
.fma-pack.zip
```

## Import safety rule

Import must be all-or-explicit-valid-only.

A failed profile or preset must not corrupt the local database. The app should validate before writing and show a readable summary.

## Import flow

1. User selects or drops a JSON/ZIP import file.
2. App inspects the file.
3. App validates every profile/preset.
4. App detects dependency issues and conflicts.
5. App shows summary.
6. User chooses import behavior.
7. App writes imported items only after final confirmation.

## ZIP pack structure

Suggested Full Alchemist Pack structure:

```text
Heroforge_Server_Pack.fma-pack.zip
  manifest.json
  profiles/
    heroforge.fma-profile.json
    reddit_gif_pack.fma-profile.json
  output_presets/
    gif_reddit_99mb.fma-output-preset.json
    gif_discord_50mb.fma-output-preset.json
    webm_vp9_1080p.fma-output-preset.json
```

## Manifest fields

```json
{
  "schema_version": "1.0",
  "kind": "full_alchemist_pack",
  "pack_name": "Heroforge Server Pack",
  "created_by": "Fullmedia Alchemist",
  "created_by_app_version": "Dev_v000.001.000_07-06-26",
  "profiles": [],
  "output_presets": [],
  "description": "Shared Heroforge conversion workflows and output presets."
}
```

## Import conflict behavior

When imported IDs already exist locally, offer:

- Import as duplicate.
- Overwrite existing.
- Keep local and skip imported.
- Cancel.

Default should be conservative: import as duplicate or cancel rather than overwrite.

## Dependency behavior

If an Alchemist Profile references Output Presets that are not already installed and not included in the bundle, the app should block or warn.

Possible choices:

- Import profile disabled until dependencies are installed.
- Import profile with missing outputs disabled.
- Cancel import.

Default should avoid creating broken active profiles.

## Public profile path behavior

Shared profiles should not include hardcoded Amanda-specific paths.

Use path variables such as:

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

The import UI should show when a profile contains absolute local paths and require confirmation or path remapping.

## Advanced JSON import

The Advanced JSON editor should use the same validation pipeline as file imports.

Bad JSON or invalid schema should fail with a popup and no save.

Example error style:

```text
Profile validation failed.

Field:
outputs[0].output_preset_id

Problem:
Referenced Output Preset does not exist and was not embedded in this import.
```
