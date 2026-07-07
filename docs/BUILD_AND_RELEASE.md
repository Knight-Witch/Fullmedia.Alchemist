# Build and Release

## Release target

Initial target is a portable Windows ZIP.

The user should only need to extract the ZIP and run:

```text
Fullmedia_Alchemist.exe
```

## Portable package structure

```text
Fullmedia_Alchemist_Portable_v0.1.0/
  Fullmedia_Alchemist.exe
  bin/
    ffmpeg.exe
    ffprobe.exe
  assets/
    icons/
    themes/
  profiles/
    defaults/
  user_data/
    config/
    logs/
    temp/
    cache/
    Converted_Originals/
  docs/
    README.md
    THIRD_PARTY_LICENSES.md
```

## FFmpeg/ffprobe

FFmpeg and ffprobe should be bundled directly with the portable release package.

Reason:

- Better user experience.
- No separate install required.
- Less setup failure.
- The app can rely on known binary paths.

Before public release, third-party license documentation must be added.

## Portable versus installed mode

The same app should eventually support both portable and installed modes.

Portable mode:

```text
App detects user_data/ beside the executable and stores writable data there.
```

Installed mode:

```text
App stores writable data in %LOCALAPPDATA%/Fullmedia Alchemist/.
```

MVP should focus on portable mode first.

## Build tooling

Recommended:

- Python.
- PySide6.
- PyInstaller one-folder build.
- Build script to assemble the portable folder.
- ZIP packaging script.

## Executable name

```text
Fullmedia_Alchemist.exe
```

## Visible app name

```text
Fullmedia Alchemist
```

## Suggested release names

```text
Fullmedia_Alchemist_Portable_v0.1.0.zip
Fullmedia_Alchemist_Setup_v0.1.0.exe
```

Installer is optional later.

## Public profile paths

Public release profiles should not include Amanda-specific local paths.

Use placeholders:

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

Dev builds may include local test profiles, but they should be marked as dev-only.

## Update system

The UI should reserve icon buttons for:

- Check for updates.
- Install downloaded update.
- Open GitHub repo.
- Open Ko-fi.
- Open Patreon.

A self-updating portable app cannot safely overwrite its own running executable directly. Later implementation should use either:

- External updater helper.
- Download + close app + run update helper/script.
- Open GitHub Releases as a fallback.
