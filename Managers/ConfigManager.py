import json
import sys
import os

_CONFIG = {}


def _fix_path_sep(path):
    """
    Set the / and \ to the current os.sep
    """
    return path.replace("\\", os.sep).replace("/", os.sep)


def _get_json_path():
    """
    Creates and returns the json config path
    """
    #Obtains the path of the program and delete CheaperSync.py from path
    json_path = sys.argv[0]
    json_path = json_path.split(os.sep)[:-1]
    json_path = os.sep.join(json_path)

    #Set slash bar in the path if any, else do not add slash bar
    json_path = f"{json_path}{os.sep}" if len(json_path) > 0 else ""
    
    json_path = f"Config{os.sep}config.json"
    return json_path


def init_config():
    """
    Inits the config and store the values in a constant
    """
    global _CONFIG
    with open(_get_json_path()) as json_file:
        _CONFIG = json.load(json_file)

        #Fix the path separator
        _CONFIG["base_path"] = _fix_path_sep(get_config("base_path"))
        _CONFIG["out_path"] = _fix_path_sep(get_config("out_path"))


def get_size_in_mb(size_in_bytes):
    """
    Transforms bytes to megabytes
    """
    return size_in_bytes / 1000000


def get_config(elem, default_value=""):
    """
    Returns the config value in a more pythonic way.
    """
    return _CONFIG.get(elem, default_value)
