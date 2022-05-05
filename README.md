# silent-Wavs
Currently only tested on Windows

A CLI python script that finds all empty/silent .WAV files in a directory and gives user the option to remove the silent files and/or move them into a new separate folder. Additionally, also gives the option of creating a `.zip` archive file to aid in uploading/sending sound stems.

For an example of running the script, see the [example](#an-example-run) at the bottom of this README.

# Helpful Articles
If you're not comfy using command-line interfaces, here's a couple documentation pages that may help you get started.
[Windows Terminal Overview](https://docs.microsoft.com/en-us/windows/terminal/)

[Running Python programs on Windows](https://docs.python.org/3/faq/windows.html#how-do-i-run-a-python-program-under-windows)

[Windows Terminal FAQ](https://github.com/microsoft/terminal/wiki/Frequently-Asked-Questions-(FAQ))

# Requirements
- Python3 (Written with Ver. 3.10.4)
- SoX | [Download Link](https://sourceforge.net/projects/sox/files/sox/) | [Home Page](http://sox.sourceforge.net/Main/HomePage)
- python pip 'sox' wrapper package

# Installation
## Downloading Files
Use one of the below methods to obtain a copy of the script.
### Using Git
If you have `git` installed, run
`git clone https://github.com/prblm-sh/silent-Wavs.git`
to clone a local copy of the repo. When the repo is finished being cloned to your machine, follow the remaining installation instructions as needed. 

### Downloading Zip
In the upper right corner at the top of this page, click the `Code` button/tab, then select `Download ZIP`. When the file finishes downloading, unzip/extract the file then follow the remaining installation instructions as needed. 

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

You may also specify the name of the directory/folder on the command line, i.e. `python silentWavs.py C:\PATH\TO\FOLDER`. If the path name contains any spaces, it must be wrapped in quotes when called from the command line. I.e. `python silentWavs.py '..\exports\new track\'`. However, when entering the folder path at the prompt when the program is running, quotes *must not be used* in the path name, even if it contains spaces.

The first prompt will ask which directory you want to check if you did not enter a directory on the command line when calling the script. Enter either the FULL path of the directory, i.e. `C:\Users\username\music\exports`.

Or you can use the relative path you're calling the script from, i.e. if your running the script from `C:\Users\username\scripts\` and the `.wav` files you want to test are in `C:\Users\username\exports\newTrack`, you can enter `..\exports\newTrack`. The `..\` indicates the parent/one directory above the current directory, in this example it would be `C:\Users\username\`. Using it twice will go up two directories. 

If you encounter an error at this step, please double-check the path you are entering and verify it is correct. 

After inputting the folder/directory for the script to scan, the script will scan every file in the directory, find files that end in `.wav`, and list the files that are silent, along with some stats from `sox` about the SILENT files. This is so the user can quickly verify all of the files the program counts as silent, are in fact, actually silent. The important values are the 'Amplitude' and 'Delta' values. For silent files, these should be `0.0`. 

Once stats have been printed out, the user is given the option to remove all of the silent files. Any files that have ANY NOISE WHATSOEVER will NOT be deleted or moved. 

If the user chooses to NOT delete the silent files, the user is given the option to move all of the SILENT files into a new, separate directory named "silentTemp" to separate the SILENT files from the files with noise. The name and location of the folder is currently hard-coded to be created in the folder the script was run on. I.e., if you run the script from `C:\Users\username\music\exports\` and enter `yes` or `y` when prompted to move silent files, the files will be moved to `C:\Users\username\music\exports\silentTemp\`. If the script was ran in `C:\Users\username\Documents\Test\`, silent files will optionally be moved to `C:\Users\username\Documents\Test\silentTemp`. 

Finally, the program will ask the user if they'd like to create a zip archive of the directory. In the case of having run an export from the 'Maschine DAW' at the sound level, this allows a user to run this script on the folder 'Maschine' created during export without having to comb through their entire arrangement to avoid empty sound files, or worse, accidently skipping a sound that was actually used. With the script, silent .wav files will be removed as fast as your computer can math, and get back a `.zip` archive ready to be uploaded as track-outs to your favorite website, favorite mix engineer, or favorite rapper. Please note, however, that if you opt to *not* delete the silent files when running the script, then create a .zip archive in the same run, the resulting archive will also contain the silent files. The `.zip` archive will be located in the parent folder of the folder that was zipped. I.e, if you create a `.zip` of `C:\Users\username\music\exports\hottestTrackEver`, the `.zip` will be located at `C:\Users\username\music\exports\hottestTrackEver.zip`, in the `exports` folder. The `hottestTracksEver` folder and all files within it will remain in place, with the exception of silent files if you choose to delete or move them during the script run. 

## An Example Run

``` powershell
PS C:\Users\producer\python\silent-Wavs> python .\silentWavs.py '..\exampleTrackouts\'

Finding .wav files in  C:\Users\producer\python\exampleTrackouts

one_shot_toast.wav
one_shot_leo_tone_drum.wav
pluck_loop_96_Gmin.wav
pluck_loop_96_Gmin.wav
ASDR Melody Sample.wav
one_shot_rolling.1.wav
Rev Drum Loop - Reversed SARZ Shaker Loop.wav
ASDR Rev Drum Loop.wav
Kick ComeOn 1.wav
Snare ComeOn 1.wav
ClosedHH ComeOn 1.wav
OpenHH ComeOn.wav
Kick ComeOn 2.wav
Snare ComeOn 2.wav
ClosedHH ComeOn 2.wav
ClosedHH ComeOn 3.wav
Chord Rhodes C ComeOn.wav
Chord Rhodes E ComeOn.wav
Chord Piano Am ComeOn.wav
Hit G ComeOn.wav
Chord Rhodes A.ComeOn.wav
Hit A ComeOn.wav
SFX ComeOn.wav
Bass C ComeOn.wav
C:\Users\producer\python\exampleTrackouts has 24 .wav Files

Checking if files are silent
13 silent files in C:\Users\producer\python\exampleTrackouts

Verify .wav files are silent
Max Amplitude values should be 0.0

pluck_loop_96_Gmin.wav : {'Maximum amplitude': 0.0}
Snare2.wav : {'Maximum amplitude': 0.0}
Snare1.wav : {'Maximum amplitude': 0.0}
ClosedHH2.wav : {'Maximum amplitude': 0.0}
ClosedHH3.wav : {'Maximum amplitude': 0.0}
Chord Rhodes C.wav : {'Maximum amplitude': 0.0}
Chord Rhodes E.wav : {'Maximum amplitude': 0.0}
Chord Piano Am.wav : {'Maximum amplitude': 0.0}
Hit G.wav : {'Maximum amplitude': 0.0}
Chord Rhodes A.wav : {'Maximum amplitude': 0.0}
Hit A.wav : {'Maximum amplitude': 0.0}
SFX.wav : {'Maximum amplitude': 0.0}
Bass C.wav : {'Maximum amplitude': 0.0}

If any amplitude values are not 0.0, please manually check tracks

If you choose to NOT remove silent files, you will be given
the option to move silent files to a separate folder.

Would you like to remove  13  silent .wav files?
Type (y)es or (N)o and press enter
y

 13 Silent .wav files will be removed
pluck_loop_96_Gmin.wav removed
Snare1.wav removed
Snare2.wav removed
ClosedHH2.wav removed
ClosedHH3.wav removed
Chord Rhodes C.wav removed
Chord Rhodes E.wav removed
Chord Piano Am.wav removed
Hit G.wav removed
Chord Rhodes A.wav removed
Hit A.wav removed
SFX.wav removed
Bass C.wav removed
Silent files removed.


Would you like to create a zip archive of files?
Original files and folders will be preserved
.zip will include silent files if they were not removed
Type (Y)es or (N)o and press enter
y

 C:\Users\producer\python\exampleTrackouts.zip file already exists
Would you like to overwrite
 C:\Users\producer\python\exampleTrackouts.zip ?
Enter (Y)es or (N)o
y

Overwriting  C:\Users\producer\python\exampleTrackouts.zip
Creating Zip Archive...
Zip archive of C:\Users\producer\python\exampleTrackouts finished.
Exiting...
```
