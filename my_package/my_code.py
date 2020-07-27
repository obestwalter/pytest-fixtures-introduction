import json
from pathlib import Path

MY_SETTINGS_PATH = Path.home() / '.my_settings'


def write_my_settings(settings):
    MY_SETTINGS_PATH.write_text(json.dumps(settings))


def read_my_settings():
    return json.loads(MY_SETTINGS_PATH.read_text())
