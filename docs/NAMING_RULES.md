# Naming Rules

## Goals

The naming system should handle messy source names, folder-based batch naming, manual overrides, output suffixes, numbering, and collision prevention.

The app should never trap users behind automatic naming. Users must be able to manually type over the convention and make that the active naming convention for the current batch/profile.

## Naming sources

Supported base-name modes:

- Auto from source filename.
- Auto from parent folder.
- Auto from selected folder.
- Manual batch name.
- Manual per-file name.

## Manual override

The naming editor should include a visible editable field for the final naming pattern.

Example:

```text
Auto-generated:
Soldier_{##}

Manual override:
WWII_Soldier_{##}
```

The app should use the manual text as the active batch convention after validation.

## Useful tokens

```text
{base}          Cleaned base name
{original}      Original source filename stem
{folder}        Parent folder name
{profile}       Alchemist Profile name
{preset}        Output Preset name
{date}          Current date
{time}          Current time
{##}            2-digit sequence number
{###}           3-digit sequence number
{height}        Output height, such as 1080
{width}         Output width when known
{codec_label}   Friendly codec label, such as vp9, av1, h264
{format}        Output format label
{extension}     Output extension without dot
```

## Cleaning behavior

Common auto-cleaning options:

- Replace spaces/hyphens with underscores.
- Remove duplicate underscores.
- Remove parentheticals.
- Remove trailing numbers.
- Remove noise words, such as `copy`.
- Title-case or preserve case.
- Strip illegal Windows filename characters.

## Noise rules

Users should be able to maintain a profile-level noise word list.

Example:

```json
{
  "noise_words": ["copy", "final", "test", "render"]
}
```

The system should support rules such as:

- Remove everything after the first `copy` token.
- Use first two words unless the second word is a noise word.
- Use folder name instead of file names for multi-file sequence outputs.

## Live preview

The naming UI must preview the output before conversion.

Example:

```text
Original:
Soldier copy copy copy.png

Cleaned base:
Soldier

Pattern:
WWII_Soldier_{##}

Preview:
WWII_Soldier_01.gif
WWII_Soldier_01.webp
WWII_Soldier_01.webm
```

## Collision handling

The app should warn when a pattern would produce collisions.

Example:

```text
Pattern: Soldier
Batch size: 12

Problem:
This pattern does not include a sequence token, so multiple outputs would use the same filename.
```

Possible actions:

- Add `{##}` automatically.
- Overwrite existing files.
- Skip duplicates.
- Cancel.

Default should be conservative: avoid overwrite unless the user explicitly confirms it.

## Output Preset suffix behavior

Output Presets may contribute suffixes or name fragments.

Examples:

```text
_REDDIT_99MB
_50MB
_1080p
-poster
```

The final naming system should combine Alchemist Profile naming with Output Preset naming fragments.

## Naming history

The app should support naming history to avoid collisions across repeated batches.

History may be global, per Alchemist Profile, or per output folder depending on settings.

The user should be able to reset or inspect naming history later if needed.
