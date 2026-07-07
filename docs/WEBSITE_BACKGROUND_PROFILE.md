# Website Background Profile

## Purpose

The Website Background Alchemist Profile is the first dev/test conversion profile.

It is based on the standalone MP4-to-multi-size-web-video conversion script currently used for Knight Witch website background media.

## Source behavior

Input:

- `.mp4` files.
- Batch process files from a source folder or drag/drop input.

Default dev profile may use local test paths. Public/default profiles must use editable path variables.

## Outputs

### AV1 WebM primary ladder

```text
2160p CRF 16
1440p CRF 18
1080p CRF 18
720p  CRF 20
```

Codec/settings:

- `libsvtav1`.
- Preset 4.
- `yuv420p`.
- No audio.
- Preserve color metadata.
- Do not upscale.

### VP9 WebM fallback ladder

```text
1080p CRF 18
720p  CRF 22
```

Codec/settings:

- `libvpx-vp9`.
- `-b:v 0`.
- `-quality good`.
- `-cpu-used 2`.
- `-row-mt 1`.
- `yuv420p`.
- No audio.
- Preserve color metadata.
- Do not upscale.

### H.264 MP4 fallback ladder

```text
1080p CRF 16
720p  CRF 18
```

Codec/settings:

- `libx264`.
- Preset slow.
- Profile high.
- `yuv420p`.
- `+faststart`.
- No audio.
- Preserve color metadata.
- Do not upscale.

### Poster WebP

- Format: WebP.
- Timestamp: 00:00:01.
- Quality: 85.
- Retry first frame if timestamp extraction fails.

## Color behavior

The workflow should preserve source color metadata where available.

Fallback SDR metadata:

```text
color primaries: bt709
color transfer: bt709
color space: bt709
color range: tv
```

## HDR / 10-bit guard

Default behavior should skip HDR or 10-bit-looking sources instead of blindly converting to SDR.

Reason: avoid washed-out/crushed color from unmanaged conversion.

Future behavior may add explicit tone-mapping options, but blind conversion should not be the default.

## Scaling behavior

- Downscale only.
- Never upscale.
- Use Lanczos scaling.
- Keep dimensions even where required by codec/container.

## Source handling

Move source MP4 to completed-source bin only after all required outputs succeed.

If any output fails, leave source in place.

## Output naming

Suggested output names:

```text
{source_stem}-{height}.av1.webm
{source_stem}-{height}.vp9.webm
{source_stem}-{height}.fallback.mp4
{source_stem}-poster.webp
```

## Required encoder checks

The app should verify bundled FFmpeg supports required encoders before running this workflow:

- `libsvtav1`
- `libvpx-vp9`
- `libx264`

If missing, fail with a clear message.
