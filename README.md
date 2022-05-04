# silent-Wavs
Currently only tested on Windows

A CLI python script that finds all empty/silent .WAV files in a directory and gives user the option to either remove the silent files or move them into a new separate folder. 

# Helpful Articles
If you're not comfy using command-line interfaces, here's a couple documentation pages that may help you get started.
[Windows Terminal Overview](https://docs.microsoft.com/en-us/windows/terminal/)

[Running Python programs on Windows](https://docs.python.org/3/faq/windows.html#how-do-i-run-a-python-program-under-windows)

# Requirements
- Python3 (Written with Ver. 3.10.4)
- SoX | [Download Link](https://sourceforge.net/projects/sox/files/sox/) | [Home Page](http://sox.sourceforge.net/Main/HomePage)
- python pip 'sox' wrapper package

# Installation
## Python
If you need to install python on your system, follow along with the [Python on Windows Docs](https://docs.python.org/3/using/windows.html), and be sure to check the 'Add Python to PATH' checkbox when installing so Python is available from cmd.exe or powershell.

If you run into an issue where trying to launch python from cmd.exe/Windows Terminal by typing `python` and pressing enter launches the windows store, you'll need to edit your PATH environment variable. Hit the 'windows' key and type 'edit environment variables'. Select the 'Path' entry in the pop-up and hit the 'Edit..' button. In the new pop-up, select the '%USERPROFILE%\AppData\Local\Microsoft\WindowsApps' entry and hit the 'Move Down' button until it is below any of the Python entries. Hit the OK button in both windows and restart your shell/terminal. 

## SoX
In order to use the Python 'sox' package, you need to have the SoX program itself installed. The download link and official project page are linked above under 'Requirements'. The program will also have to be added to your systems PATH. [This tutorial](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/) walks through the process.

Hit the 'Windows' key and search 'Edit environment variables' and select 'Edit environment variables for your account'. In the upper part of the window, select/highlight the 'Path' entry and hit the 'Edit..' button. In the new pop-up, select 'New', and enter "C:\Program Files (x86)\sox-14-4-2" (with no quotes), verify the version number is correct. Click 'OK' in both windows. If you have any shells or IDE's open, close and restart them for the environment variable change to take effect. 

## Python pip sox wrapper package
To install the `sox` package, in your terminal run `pip install sox`, or from within the project folder, run `pip install -r requirements.txt`. This should also download and install any dependencies for the `sox` package.

# Usage
To run the script, from a terminal/CLI run `python silentWavs.py`
If you're running the script from a different directory, use `python C:\PATH\TO\SCRIPT\silentWavs.py`, replacing `\PATH\TO\SCRIPT` with where it's been saved on yoru system.

The first prompt will ask which directory you want to check. Enter either the FULL path of the directory, i.e. `C:\Users\username\music\exports`.

Or you can use the relative path you're calling the script from, i.e. if your running the script from `C:\Users\username\scripts\` and the `.wav` files you want to test are in `C:\Users\username\exports\newTrack`, you can enter `..\exports\newTrack`. The `..\` indicates the parent/one directory above the current directory, in this example it would be `C:\Users\username\`. Using it twice will go up two directories. 

If you encounter an error at this step, please double-check the path you are entering and verify it is correct. 

After inputting the folder/directory for the script to scan, the script will scan every file in the directory, find files that end in `.wav`, and list the files that are silent, along with some stats from `sox` about the SILENT files. This is so the user can quickly verify all of the files the program counts as silent, are in fact, actually silent. The important values are the 'Amplitude' and 'Delta' values. For silent files, these should be `0.0`. 

Once stats have been printed out, the user is given the option to remove all of the silent files. Any files that have ANY NOISE WHATSOEVER will NOT be deleted or moved. 

If the user chooses to NOT delete the silent files, the user is given the option to move all of the SILENT files into a new, separate directory named "silentTemp" to separate the SILENT files from the files with noise. The name and location of the are currently hard-coded to be created in the folder the script was run on. I.e., if you run the script from `C:\Users\username\music\exports\` and enter `yes` or `y` when prompted to move silent files, the files will be moved to `C:\Users\username\music\exports\silentTemp\`. If the script was ran in `C:\Users\username\Documents\Test\`, silent files will optionally be moved to `C:\Users\username\Documents\Test\silentTemp`. 