import json
import sys
import os

_CONFIG = {}


def _get_json_path():
    """
    Creates and returns the json config path
    """
    json_path = sys.argv[0]
    json_path = json_path.split(os.sep)[:-1]
    json_path = os.sep.join(json_path)
    json_path = f"{json_path}{os.sep}Config{os.sep}config.json"
    return json_path


def init_config():
    """
    Inits the config and store the values in a constant
    """
    global _CONFIG
    with open(_get_json_path()) as json_file:
        _CONFIG = json.load(json_file)


def get_size_in_mb(size_in_bytes):
    """
    Transforms bytes to megabytes
    """
    return size_in_bytes / 1000000


def get_config(elem, default_value=None):
    """
    Returns the config value in a more pythonic way.
    """
    return _CONFIG.get(elem, default_value)
