import os
from glob import glob

import Managers.ConfigManager as cm


def _filter_files(paths):
    """
    Remove paths that does not have selected extensions or exceeds size thresholds.
    """
    filtered_paths = [path for path in paths if cm.get_config(
        "out_path") not in path for ext in cm.get_config("file_extensions") if ext in path.split(".")[-1]]
    filtered_paths = [path for path in filtered_paths if cm.get_size_in_mb(
        os.path.getsize(path)) <= cm.get_config("size_threshold_in_MB", 100)]

    return filtered_paths


def _get_subdirs(paths):
    """
    Returns the dirs inside the paths.
    """
    paths = [glob(f"{path}{os.sep}*") for path in paths]
    paths = [p for glob_path in paths for p in glob_path if os.path.isdir(p)]

    return paths


def _get_base_paths_to_check():
    """
    Returns all the possible base paths to check.
    """
    selected_folders = cm.get_config("selected_folders")
    base_paths = [cm.get_config("base_path", os.path.abspath(os.sep))] if len(selected_folders) == 0 \
        else [f"{cm.get_config('base_path', '')}{os.sep}{folder}" for folder in selected_folders]

    upgraded_base_paths = _get_subdirs(base_paths)

    return upgraded_base_paths, base_paths


def get_files_paths():
    """
    Memory-effienctly yields files to be copied from selected paths. 
    """
    upgraded_base_paths, base_paths = _get_base_paths_to_check()

    # Get files from base paths only for its first level.
    for path in base_paths:
        print(f"Obteniendo archivos de: {path}")
        paths = glob(f"{path}{os.sep}*.*")
        paths = _filter_files(paths)

        yield paths

    # Get files from all upgraded paths (one level inside base_paths) recursively.
    for path in upgraded_base_paths:
        print(f"Obteniendo archivos de: {path}")
        paths = glob(f"{path}{os.sep}**{os.sep}*.*", recursive=True)
        paths = _filter_files(paths)

        yield paths
