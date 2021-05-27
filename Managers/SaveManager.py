import shutil
import os

import Managers.ConfigManager as cm


def _get_file_size(file_path):
    """
    Tries to obtain the file size. If it is hidden then returns
    placeholder value.

    Params:
        - file_path (string): file path to get the size.

    Returns:
        - file size (numeric)
    """
    try:
        return os.path.getsize(file_path)
    except:
        return cm.get_config("size_threshold_in_MB") + 1


def _filter_files(paths):
    """
    Remove paths that does not have selected extensions, exceeds size threshold, 
    is in out_path or in an ignored folder.

    Params:
        - paths (list[string]): file paths to filter.
    """
    for path in paths:
        #Check not in out path
        if (cm.get_config("out_path") not in path):
            #Check not exceeds threshold
            if cm.get_size_in_mb(_get_file_size(path)) <= cm.get_config("size_threshold_in_MB"):
                #Check not in ignored folder
                is_in_ignored_folder = False
                for ignored_folder in cm.get_config("ignored_folders"):
                    if ignored_folder in path:
                        is_in_ignored_folder = True
                #Check contains valid extension
                if not is_in_ignored_folder:
                    for file_extension in cm.get_config("file_extensions"):
                        if path.endswith(file_extension):
                            copy_file(path)


def copy_file(path_from):
    """
    Creates the subdirectories in destination folder and upload the file if it was not already uploaded.

    Params:
        - path_from (string): path that contains the file to copy. 
    """
    file_path = path_from
    for base_path in cm.get_config("base_paths"):
        file_path = file_path.replace(base_path, "")

    out_path = cm.get_config("out_path")
    path_to = f"{out_path}{os.sep}{file_path}"

    full_out_path = os.sep.join(path_to.split(os.sep)[:-1])
    if not os.path.exists(full_out_path):
        os.makedirs(full_out_path)

    last_modified_from = os.stat(path_from).st_mtime
    last_modified_to = os.stat(
        path_to).st_mtime if os.path.isfile(path_to) else 0

    if last_modified_from > last_modified_to:
        print(f"Copying file {path_from}")
        try:
            shutil.copyfile(path_from, path_to)
        except Exception as e:
            print(e)


def copy_files():
    """
    Walk for each base_path and save the file in out_path.
    """
    for base_path in cm.get_config("base_paths"):
        for root, _, files in os.walk(base_path):
            file_paths = [f"{root}{os.sep}{file}" for file in files]
            _filter_files(file_paths)
