import json
import sys
import os

import Managers.ErrorManager as em


_CONFIG = {}


def _get_json_path():
    """
    Creates and returns the json config path.

    Returns:
        - json_path (string): the path of the json
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


def get_size_in_mb(size_in_bytes):
    """
    Transforms bytes to megabytes

    Params:
        - size_in_bytes (numeric)
    
    Returns:
        - size_in_bytes transformed to mb 
    """
    return size_in_bytes / 1000000


def _get_config_default_value(elem):
    """
    Returns the default config value.

    Params:
        - elem (string): config key.

    Returns:
        - default value for selected key (type depends on elem)
    """
    if elem == "base_paths":
        em.showError("base_paths value needed", let_copy=False)
    elif elem == "ignored_folders":
        return []
    elif elem == "out_path":
        return f"{os.getcwd()}{os.sep}stored_data"
    elif elem == "file_extensions":
        return ["txt", "pdf", "docx", "doc", "csv"]
    elif elem == "size_threshold_in_MB":
        return 50


def get_config(elem):
    """
    Returns the config value in a more pythonic way.

    Params:
        - elem (string): config key

    Returns:
        - config value for selected key or default if not exists (string) 
    """
    elem_value = _CONFIG.get(elem)
    return _get_config_default_value(elem) if elem_value is None else elem_value