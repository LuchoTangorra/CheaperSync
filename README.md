# Cheaper Sync

Cheaper sync is a free software that stores your files with desired extension (prefered text files only) in a folder, so you can upload them to the cloud of your choice. It works on any operative system.

The objetive of this project is to save money in cloud storage uploading only the selected files. It could also be used to store all the files with the selected extensions in one unique folder. 

This free software is used by travel agencies in Buenos Aires, Argentina. 

### Project structure

- CheaperSync.py: contains all the python code to excecute.
- config.json: contains the necessary initial configuration. This should be manually setted as follows:
	- base_path: start path. The process will start searching from and inside this path.
	- important_folders: base path subfolders. The process will only search inside this folders, ignoring any other  folder in base path.
	- out_path: path when the data will be stored, if inside base path it will be ignored when searching. The data will be stored in this folder but the process will recreate the same folder structure that contains the original path.
	- extensions: only files with those extensions will be saved in out path.
	- size\_threshold_in\_MB: ignore files that has a size above this threshold.
	
### How to use
- Linux:
	- Minimun requirements: python3 installed. 
	- Go to the CheaperSync path.
	- Set your desired configuration in the config.json file.  
	- Run: python3 CheaperSync.py
	
- Windows:
	- Minimun requirements: pyinstaller installed (if deploy as .exe), python3 installed (if used as-is from cmd follow linux instructions).
	- Go to the CheaperSync path.
	- Run: pyinstaller CheaperSync.py --noconsole
	- The scrit above will create a .exe. Run it to run the program.
