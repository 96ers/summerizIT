"""Configs module."""

import os

from dotenv import load_dotenv

load_dotenv()


def get_env(key: str) -> str:
    """Get the environment variable value."""
    return os.environ[key]
