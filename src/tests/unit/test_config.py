import os


def test_primary_config(test_app):
    """
    Test that the development configuration is loaded correctly.
    """
    test_app.config.from_object("src.config.Config")
    assert test_app.config["SECRET_KEY"] == "default_secret_key"
    assert not test_app.config["TESTING"]


def test_testing_config(test_app):
    """
    Test that the testing configuration is loaded correctly into the Flask app.
    """
    app_config = test_app.config

    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == "default_secret_key"
    assert test_app.config["TESTING"]
    assert "OPENAI_API_KEY" in app_config
