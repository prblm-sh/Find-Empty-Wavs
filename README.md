# silent-Wavs
Currently only tested on Windows

A python script that finds all empty/silent .WAV files in a directory and, optionally, moves them to a new directory and/or removes them.

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