import shutil
import os

import Managers.ConfigManager as cm


def _copy_file(path_from):
    """
    Creates the subdirectories in destination folder and upload the file if it was not already uploaded.
    """
    file_path = path_from.replace(cm.get_config("base_path", ""), "")

    out_path = cm.get_config("out_path", f"{os.getcwd()}{os.sep}stored_data")
    path_to = f"{out_path}{os.sep}{file_path}"

    full_out_path = os.sep.join(path_to.split(os.sep)[:-1])
    if not os.path.exists(full_out_path):
        os.makedirs(full_out_path)

    last_modified_from = os.stat(path_from).st_mtime
    last_modified_to = os.stat(path_to).st_mtime if os.path.isfile(path_to) else 0

    if last_modified_from > last_modified_to:
        print(f"Copying file {path_from}")
        try:
            shutil.copyfile(path_from, path_to)
        except Exception as e:
            print(e)


def copy_files(files_paths):
    """
    Copy all the files in out_path folder.
    """
    list(map(_copy_file, files_paths))
