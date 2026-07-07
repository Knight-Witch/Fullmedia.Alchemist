"""Internal tool metadata registry.

The UI footer/status bar uses this registry to display subtle version metadata when a user
hovers over registered tools, panels, and functions.
"""

from __future__ import annotations

from dataclasses import dataclass

from fullmedia_alchemist.version import APP_VERSION


@dataclass(frozen=True)
class ToolMetadata:
    """Metadata shown in the footer/status bar for internal tools."""

    tool_id: str
    name: str
    version: str
    description: str


TOOLS: dict[str, ToolMetadata] = {
    "app_shell": ToolMetadata(
        tool_id="app_shell",
        name="App Shell",
        version=APP_VERSION,
        description="Main PySide6 application shell.",
    ),
    "profile_validator": ToolMetadata(
        tool_id="profile_validator",
        name="Profile Validator",
        version=APP_VERSION,
        description="JSON validation for Alchemist Profiles and Output Presets.",
    ),
    "conversion_engine": ToolMetadata(
        tool_id="conversion_engine",
        name="Conversion Engine",
        version=APP_VERSION,
        description="FFmpeg-backed conversion planning and execution.",
    ),
    "gif_optimizer": ToolMetadata(
        tool_id="gif_optimizer",
        name="GIF Optimizer",
        version=APP_VERSION,
        description="Temporary candidate encoding and size-targeted GIF optimization.",
    ),
    "naming_engine": ToolMetadata(
        tool_id="naming_engine",
        name="Naming Engine",
        version=APP_VERSION,
        description="Naming cleanup, token expansion, previews, and collision handling.",
    ),
    "website_background_profile": ToolMetadata(
        tool_id="website_background_profile",
        name="Website Background Profile",
        version=APP_VERSION,
        description="Multi-size AV1/VP9/MP4/WebP website background workflow.",
    ),
}


def get_tool_metadata(tool_id: str) -> ToolMetadata | None:
    """Return registered metadata for a tool identifier."""
    return TOOLS.get(tool_id)
