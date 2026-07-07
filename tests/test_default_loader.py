from fullmedia_alchemist.profiles import load_default_content


def test_default_content_loads_without_validation_issues():
    content = load_default_content()

    assert content.is_valid
    assert len(content.profiles) >= 1
    assert len(content.output_presets) >= 1


def test_website_background_profile_references_existing_presets():
    content = load_default_content()

    preset_ids = {preset.preset_id for preset in content.output_presets}
    profile = next(
        profile for profile in content.profiles if profile.profile_id == "website_background"
    )

    assert set(profile.output_preset_ids).issubset(preset_ids)
