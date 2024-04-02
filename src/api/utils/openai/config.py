from flask import current_app
import os

os.getenv("OPENAI_API_KEY")


def get_openai_key():
    return current_app.config.get('OPENAI_API_KEY')
