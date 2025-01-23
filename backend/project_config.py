import os
from dotenv import load_dotenv


def setup_openai_config():
    import openai
    openai.api_key = '123'
    openai.organization = '456'


def setup_app_config():
    load_dotenv()
    setup_openai_config()
