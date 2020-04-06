from dotenv import load_dotenv
from os.path import join, dirname
import os

env_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

BROWSER = os.getenv("BROWSER")
URL = os.getenv("URL")
INVALID_EMAIL = os.getenv("INVALID_EMAIL")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")