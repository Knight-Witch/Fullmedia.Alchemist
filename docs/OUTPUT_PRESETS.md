# Output Presets

## Meaning

An **Output Preset** is a reusable file-output recipe.

It is separate from an Alchemist Profile so users can create useful output targets once and reuse them across multiple profiles.

Examples:

- GIF - Reddit 99MB.
- GIF - Discord 50MB.
- WebM - VP9 1080p.
- WebM - AV1 2160p.
- MP4 - H.264 Fallback 1080p.
- Poster - WebP 85.

## Why Output Presets exist

A user may want to use `GIF - Reddit 99MB` inside multiple Alchemist Profiles without rebuilding the same settings every time.

Example:

```text
Alchemist Profile: Heroforge
  Output Presets:
    - GIF - Reddit 99MB
    - GIF - Discord 50MB
    - WebM - VP9 1080p

Alchemist Profile: Knight Witch Apparel
  Output Presets:
    - GIF - Reddit 99MB
    - WebM - VP9 1080p
    - Poster - WebP 85
```

## Required conceptual fields

```json
{
  "schema_version": "1.0",
  "kind": "output_preset",
  "preset_id": "gif_reddit_99mb",
  "preset_name": "GIF - Reddit 99MB",
  "preset_version_id": "opv_000001_07-06-26_1900",
  "format": "gif",
  "description": "Creates a GIF optimized under Reddit's 100 MB limit.",
  "settings": {},
  "metadata": {}
}
```

## Multiple outputs of the same file type

The app must support multiple Output Presets of the same output format inside one Alchemist Profile.

Example:

```text
Source: animation.mp4
Outputs:
  animation_REDDIT_99MB.gif
  animation_50MB.gif
  animation_PREVIEW_10MB.gif
  animation_1080p.vp9.webm
```

Do not model output formats as single booleans like `make_gif: true` in the profile. Use a list of output preset references.

## GIF size-capped preset behavior

A GIF Output Preset may include:

```json
{
  "format": "gif",
  "max_bytes": 103809024,
  "quality_policy": "fidelity_first_under_cap",
  "optimizer": {
    "strategy": "test_encode_search",
    "preserve_fps": true,
    "allow_fps_reduction": false,
    "min_dimension": 400,
    "dimension_step": 16,
    "scale_filter": "lanczos",
    "palette_mode": "high_quality"
  }
}
```

The engine should create temporary candidates, measure file size, and keep revising until it finds the best acceptable output under the cap.

## Video ladder preset behavior

A video Output Preset may represent one output or a ladder.

Example ladder:

```json
{
  "format": "webm",
  "codec": "libsvtav1",
  "label": "AV1 WebM Ladder",
  "ladder": [
    {"height": 2160, "crf": 16},
    {"height": 1440, "crf": 18},
    {"height": 1080, "crf": 18},
    {"height": 720, "crf": 20}
  ]
}
```

The app may either treat a ladder as one multi-output preset or expose each ladder rung as a generated child output. The UI should make it clear how many files will be produced.

## Preset version history

Output Presets should maintain their own version history.

Useful behavior:

- Rollback.
- Roll-forward.
- Duplicate preset.
- Export preset.
- Compare later if implemented.
- Detect profiles using older locked preset versions.

## Profile usage behavior

When adding an Output Preset to an Alchemist Profile, the user should be able to choose:

- Link to preset.
- Copy/snapshot into profile.

Default should favor locked/snapshot behavior unless the user explicitly wants live/latest preset updates.

## Import/export

Output Presets should be importable/exportable independently from Alchemist Profiles.

Supported package types:

- Single Output Preset JSON.
- Output Preset Bundle ZIP.
- Full Alchemist Pack ZIP containing profiles plus presets.

## Validation rules

Reject Output Presets when:

- JSON is malformed.
- `kind` is not `output_preset`.
- Required fields are missing.
- Format is unsupported.
- Codec is unsupported.
- CRF/quality values are invalid.
- Dimensions are invalid.
- Size caps are invalid.
- Naming fragment would cause unavoidable collisions.
- Executable/script content is detected.
