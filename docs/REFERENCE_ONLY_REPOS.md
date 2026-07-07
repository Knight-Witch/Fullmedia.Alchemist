# Reference-Only Repositories

## Rule

Only the `Fullmedia.Alchemist` repository is edited for this project.

Other repositories may be reviewed for UX, architectural, or asset reference, but must not be modified, patched, committed to, cleaned up, or reorganized as part of this project.

## Reference-only examples

- Witch Dock.
- Witch Tools.
- Witch Quickbar.
- Witch Dev.
- Blender tools repositories.
- Heroforge scripts repositories.
- Any other prior conversion-script or UI-project repositories unless explicitly moved into this repo.

## Asset copying

Icons/assets may be copied from existing repositories into Fullmedia Alchemist only when needed.

When this happens:

- Copy the asset into this repo's `assets/` tree.
- Do not edit the source repository.
- Track the copied asset in this repo.
- Confirm licensing/ownership before public release.

## Legacy scripts

Legacy conversion scripts should be copied into this repo under a `legacy/` folder if they are needed as implementation references.

The production app should not directly depend on those scripts as independent console utilities. Their logic should be extracted into reusable modules.
