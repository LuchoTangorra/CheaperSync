#!/usr/bin/env python
# coding: utf-8

"""
Owner: Luciano Tangorra

Modified: 2021/05/23

Cheaper sync is a free software that stores your files with desired 
extension in a folder, so you can upload them to the cloud of your choice.

It works on any operative system!
"""

from glob import glob
import os
import sys
import json
import shutil
import time


CONFIG = {}

def init_config():
    """
    Inits the config and store the values in a constant
    """
    global CONFIG
    with open('config.json') as json_file:
        CONFIG = json.load(json_file)
    
    
def get_size_in_mb(size_in_bytes):
    """
    Transforms bytes to megabytes
    """
    return size_in_bytes / 1000000


def copy_file(path_from):
    """
    Creates the subdirectories in destination folder and upload the file if it was not already uploaded.
    """    
    file_path = path_from.replace(CONFIG.get("base_path", ""), "")
    
    out_path = CONFIG.get("out_path", f"{os.getcwd()}{os.sep}stored_data")
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
    list(map(copy_file, files_paths))
    
    
def filter_files(paths):
    """
    Remove paths that does not have selected extensions or exceeds size thresholds.
    """
    filtered_paths = [path for path in paths if CONFIG.get("out_path") not in path for ext in CONFIG.get("extensions") if ext in path.split(".")[-1]]
    filtered_paths = [path for path in filtered_paths if get_size_in_mb(os.path.getsize(path)) <= CONFIG.get("size_threshold_in_MB", 100)]

    return filtered_paths
            

def get_more_dirs(paths):    
    """
    Returns the dirs inside the paths.
    """
    paths = [glob(f"{path}{path.sep}*") for path in paths]
    paths = [p for glob_path in paths for p in glob_path if os.path.isdir(p)]
    
    return paths
    
    
def get_base_paths_to_check():
    """
    Returns all the possible base paths to check.
    """
    important_folders = CONFIG.get("important_folders")
    base_paths = [CONFIG.get("base_path", os.path.abspath(os.sep))] if len(important_folders) == 0 \
                else [f"{CONFIG.get('base_path', '')}{os.sep}{folder}" for folder in important_folders]
    
    upgraded_base_paths = get_more_dirs(base_paths)
    
    return upgraded_base_paths, base_paths


def get_files_paths():
    """
    Memory-effienctly yields files to be copied from selected paths. 
    """
    upgraded_base_paths, base_paths = get_base_paths_to_check()
    
    #Get files from base paths only for its first level.
    for path in base_paths:
        print(f"Obteniendo archivos de: {path}")
        paths = glob(f"{path}{os.sep}*.*")
        paths = filter_files(paths)

        yield paths
        
    #Get files from all upgraded paths (one level inside base_paths) recursively.
    for path in upgraded_base_paths:
        print(f"Obteniendo archivos de: {path}")
        paths = glob(f"{path}{os.sep}**{os.sep}*.*", recursive=True)
        paths = filter_files(paths)

        yield paths


def main():
    os.makedirs(CONFIG.get("out_path", ""))

    for paths in get_files_paths():
        copy_files(paths)


if __name__ == "__main__":
    print("Iniciando ejecucion...\n")
    init_config()
    main()