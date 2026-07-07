# Conversion Engine

## Principle

The conversion engine should be independent of the UI.

The UI selects Alchemist Profiles and Output Presets. The engine probes inputs, builds conversion plans, runs FFmpeg/ffprobe, manages temp files, measures outputs, and reports progress/results.

## Required capabilities

- File/folder/archive input.
- Batch queue.
- Media probing via ffprobe.
- FFmpeg command generation.
- Progress parsing.
- Temporary output management.
- Size-targeted optimizer loops.
- Dependency-aware output graph.
- Source movement only after successful conversion.
- Failure-safe source handling.

## Quality priority

Default quality policy should be fidelity-first.

Primary priorities:

1. Color fidelity.
2. Correct dimensions/aspect ratio.
3. Resolution.
4. Framerate/source timing.
5. File size.

When a hard cap exists, find the highest-fidelity candidate under the cap without crossing profile-defined minimum boundaries.

If impossible, fail clearly and explain why.

## GIF size targeting

GIF Output Presets should support temporary candidate encoding.

Generic loop:

1. Probe source.
2. Generate palette where applicable.
3. Encode temporary candidate.
4. Measure file size.
5. If over cap, revise candidate settings.
6. If under cap, attempt better/larger candidate when applicable.
7. Select best acceptable candidate.
8. Produce final output.
9. Clean temp files.
10. Log selected settings.

Candidate variables may include:

- Resolution.
- Long-edge dimension.
- FPS if profile allows it.
- Palette mode.
- Dither mode.
- Quality/compression setting if applicable.

The app should not silently produce potato-quality output to satisfy a cap.

## PNG sequence handling

PNG series workflows should:

- Natural-sort frames.
- Stage frames into a clean sequence such as `frame_%06d.png`.
- Preserve source timing or apply profile FPS.
- Generate requested Output Presets.
- Optionally keep or delete staged/intermediate files depending on profile settings.

## Website Background workflow

The first real workflow to wire into the app should be based on the current website-background conversion script.

Behavior:

- Input: MP4.
- Generate AV1 WebM ladder.
- Generate VP9 WebM fallback ladder.
- Generate H.264 MP4 fallback ladder.
- Generate WebP poster.
- Remove audio.
- Do not upscale.
- Use Lanczos scaling.
- Preserve source color metadata when present.
- Use SDR fallback metadata of bt709/tv where needed.
- Skip HDR/10-bit-looking sources by default to avoid damaging color fidelity with blind SDR conversion.
- Move source to completed-source bin only after all required outputs succeed.

## Dependency-aware output graph

The engine should eventually support conversion dependencies.

Example:

```text
Source PNG sequence
  -> staged frames
  -> intermediate mezzanine MP4
  -> WebM outputs
  -> GIF outputs
```

This should be profile-controlled and engine-decided where appropriate. Not every workflow should use intermediates.

## Source handling

Supported source behavior:

- Leave in place.
- Move after success.
- Copy after success.
- Rename as done.
- Archive to app default `Converted_Originals` folder.
- Archive to output-folder `Converted_Originals` folder.
- Archive to custom folder.

Default if move/archive is enabled but no destination is specified:

```text
user_data/Converted_Originals/
```

Failed conversions should leave sources in place.

## Progress reporting

The engine should report:

- Current job.
- Current output.
- Current step.
- Percent when calculable.
- Elapsed time.
- ETA.
- Expected finish timestamp.
- Current candidate dimensions/settings for optimizer jobs.
- Best successful candidate so far for optimizer jobs.
- FFmpeg failure details.

## FFmpeg binary handling

The app should prefer bundled FFmpeg/ffprobe in release builds.

Development may allow custom paths, but the default user experience should not require installing FFmpeg separately.
