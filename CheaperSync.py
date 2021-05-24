#!/usr/bin/env python
# coding: utf-8

"""
Owner: Luciano Tangorra

Modified: 2021/05/23

Cheaper sync is a free software that stores your files with desired 
extension in a folder, so you can upload them to the cloud of your choice.

It works on any operative system!
"""

import os

import Managers.ConfigManager as cm
import Managers.PathManager as pm
import Managers.SaveManager as sm


def process():
    """
    Main process function.
    """
    out_path = cm.get_config("out_path", "")
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    for paths in pm.get_files_paths():
        sm.copy_files(paths)


if __name__ == "__main__":
    print("Iniciando ejecucion...\n")
    cm.init_config()
    process()
