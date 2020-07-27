"""Classic tests - no fixtures"""
import json
import tempfile
from pathlib import Path

from my_package import my_code


def test_read_my_settings_no_fixtures():
    """Make sure that settings are read correctly."""
    old_path = my_code.MY_SETTINGS_PATH
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            my_code.MY_SETTINGS_PATH = Path(tmpdir) / '.my_fake_settings'
            fake_settings = {'name': 'Paul'}
            my_code.MY_SETTINGS_PATH.write_text(json.dumps(fake_settings))
            assert my_code.read_my_settings() == fake_settings
    finally:
        my_code.MY_SETTINGS_PATH = old_path


def test_write_my_settings_no_fixtures():
    """Make sure that settings are written correctly."""
    old_path = my_code.MY_SETTINGS_PATH
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            my_code.MY_SETTINGS_PATH = Path(tmpdir) / '.my_fake_settings'
            fake_settings = {'name': 'Oliver'}
            my_code.write_my_settings(fake_settings)
            retrieved_settings = my_code.MY_SETTINGS_PATH.read_text()
            assert eval(retrieved_settings) == fake_settings
    finally:
        my_code.MY_SETTINGS_PATH = old_path
