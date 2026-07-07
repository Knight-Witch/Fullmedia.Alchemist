from fullmedia_alchemist.version import APP_NAME, APP_VERSION, EXECUTABLE_NAME


def test_app_metadata():
    assert APP_NAME == "Fullmedia Alchemist"
    assert APP_VERSION.startswith("Dev_v")
    assert EXECUTABLE_NAME == "Fullmedia_Alchemist.exe"
