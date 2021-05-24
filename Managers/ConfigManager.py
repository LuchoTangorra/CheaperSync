import json

CONFIG = {}

def init_config():
    """
    Inits the config and store the values in a constant
    """
    global CONFIG
    with open('Config/config.json') as json_file:
        CONFIG = json.load(json_file)


def get_size_in_mb(size_in_bytes):
    """
    Transforms bytes to megabytes
    """
    return size_in_bytes / 1000000


def get_config(elem, default_value=None):
    """
    Returns the config value in a more pythonic way.
    """
    return CONFIG.get(elem, default_value)