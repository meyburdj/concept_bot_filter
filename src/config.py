import os

class Config:
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class TestingConfig():
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    OPENAI_API_KEY = "this_is_a_fake_key"
    TESTING = True