# Cheaper Sync

Cheaper sync is a free software that stores your files with desired extension (prefered text files only) in a folder, so you can upload them to the cloud of your choice. It works on any operative system.

The objetive of this project is to save money in cloud storage uploading only the selected files. It could also be used to store all the files with the selected extensions in one unique folder (or external disk). 

This free software is used by travel agencies in Buenos Aires, Argentina.

### Project structure

- CheaperSync.py: contains the main program.
- Managers: contains the managers used in the main program.
	- ConfigManager: control the config set by the user.
	- PathManager: generates the file paths requested in the config file.
	- SaveManager: store the previously selected files in a new folder and/or in the cloud (not implemented yet). 

### Set config:
Go to Config folder and modify config.json, which params works as follows:
- base_path: start path. The process will start searching from and inside this path.
- important_folders: base path subfolders. The process will only search inside this folders, ignoring any other  folder in base path.
- out_path: path when the data will be stored, if inside base path it will be ignored when searching. The data will be stored in this folder but the process will recreate the same folder structure that contains the original path.
- file\_extensions: only files with those extensions will be saved in out path.
- size\_threshold\_in\_MB: ignore files that has a size above this threshold.

For the application to work you need to have Config/config.json on the same folder as CheaperSync.py or CheaperSync.exe

_For Windows users_: it is important not to use "\\" in your paths, use "/" or "\\\\" instead.

### How to use

In both cases you should set your configuration in the config.json file inside Config folder.  

- Linux:
	- Minimun requirements: python3 installed. 
	- Go to the CheaperSync path.
	- Run: python3 CheaperSync.py
	
- Windows:
To run this program on Windows you have two posibilities:
	- Run with python (same instructions as on Linux).
	- Download the .exe and config file from here: https://drive.google.com/file/d/1i6avr_GvV8-XO7pSK3EMuOz0ipsJ-xVq/view?usp=sharing . Set the config and run the .exe.
	
### How to schedule
The following instructions will set the CheaperSync to run each time the computer is booted.

- Linux:
	- Create a .sh that contains the following command: python3 {path\_to\_cheaper\_sync}/CheaperSync.py
	- Move that .sh to /etc/init.d/
	- Make sure it is executable by: sudo chmod +x /etc/init.d/{sh\_file\_name.sh}
	- Run this command: sudo update-rc.d {sh\_file\_name.sh} defaults

- Windows:
	- Press windows key + R
	- Run the command: Shell:startup
	- It will reach C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
	- Copy and paste the shortcut to the app from the file location to the Startup folder.
	- You can check if it was correctly setted by restarting the PC and go to task manager (CTRL+ALT+DEL). Go to Startup and check if the app is enabled (it should).
