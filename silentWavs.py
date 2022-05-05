import os
import shutil
import sox
import sys


# Check if user entered folder name arg on command line
if len(sys.argv) == 2:
    path = (sys.argv[1])
    # String manipulation to remove quote chars from
    # folder names that contain spaces.
    path = path.replace('"', '')
    workDir = os.path.abspath(path)
    os.chdir(workDir)

# If no argument was entered
elif len(sys.argv) == 1:
    # Get user input for working directory
    print("\nPlease enter path to folder")
    print("If folder path contains spaces, DO NOT")
    print("put quote characters in your input.\n")
    path = input("Press Enter to use current directory\n")
    # If no input, use current directory
    if len(path) <= 0:
        workDir = os.path.abspath(os.getcwd())
    else:
        workDir = os.path.abspath(path)
        os.chdir(workDir)

# If too many arguments, notify user and exit
elif len(sys.argv) >= 3:
    print("Too many many arguments. Only enter one directory at a time\nExiting..")
    exit()

# get LIST of files in current working directory
files = os.listdir()

# Empty list to hold .wav files
wavList = []

print("\nFinding .wav files in ", workDir, "\n")

# Only work with .wav files
for file in files:
    if file.endswith(".wav"):
        wavList.append(file)
        print(file)

# Get number of .wav files in directory
numOfWavs = len(wavList)

print(workDir, "has",  numOfWavs, ".wav Files \n")


# Empty list for SILENT Files
silentWavs = []

# for every file in wavList, check if silent
# 2nd arg in silent() is threashold for 
# determining silence. Set so that a track
# with ANY amplitude AT ALL will not be touched
print("Checking if files are silent")
for wav in wavList:
    if sox.file_info.silent(wav, 0.0000000000000001):
        silentWavs.append(wav)

# If no .wav files are found, notify user and exit
if len(wavList) == 0:
    print("No .wav files found in ", workDir, "\nExiting...")
    exit()

# If no silent .wav files are found, notify user
if len(silentWavs) == 0:
    print("No SILENT .wav files found.\n")

elif len(silentWavs) >= 1:
    numOfSilentWavs = len(silentWavs)
    print(numOfSilentWavs, "silent files in", workDir, "\n")

    # Prints various stats about silent .wav files
    # Amp values should be 0.0 silent files
    print("Verify .wav files are silent")
    print("Max Amplitude values should be 0.0\n")

    # get only amplitude values from sox.file_info.stats()
    for x in silentWavs:
        stat = sox.file_info.stat(x)
        maxAmp = dict((a, stat[a]) for a in ['Maximum amplitude'] if a in stat)
        print(x, ":", maxAmp)

    print("\nIf any amplitude values are not 0.0, please manually check tracks\n")


    # prompt for deletion of silent files
    print("If you choose to NOT remove silent files, you'll be given")
    print("the option to move silent files to a separate folder.")
    print("\nWould you like to remove ", numOfSilentWavs, " silent .wav files?")
    delAnswer = input("Type (y)es or (N)o and press enter\n").upper()

    # If user answers No, don't touch files and exit
    if delAnswer[0] == "N":
        print("\nFiles Not Deleted\n")

    # If user answers yes
    elif delAnswer[0] == "Y":
        print("\n", numOfSilentWavs, "Silent .wav files will be removed")
        for w in silentWavs:
            os.remove(w)
            print(w, "removed")
        print("Silent files removed.\n")

    else:
        print("\nIncorrect input. No files deleted. Exiting...")
        exit()


    if delAnswer[0] == "N":
        # Prompt for moving silent files to new directory
        # to separate them from LOUD files for verification
        print("Would you like to move ", numOfSilentWavs, " silent files to a separate directory?")
        movAnswer = input("Type (Y)es or (N)o and press enter\n").upper()

        # Directory variables for move file loops
        sourceDir = workDir
        tempDir = "silentTemp"
        newDir = os.path.join(sourceDir, tempDir)

        # If No, leave files in original directory
        if movAnswer[0] == "N":
            print("\nLeaving files in original folder.\n")

        # If Yes, create new directory and move files
        elif movAnswer[0] == "Y":
            # Check if directory exists already
            # If dir exists, continue and move files
            if os.path.exists(newDir) == True:
                print(newDir, " already exists. Moving Files\n")
            # If dir */DOES NOT/* exist, create it
            elif os.path.exists(newDir) == False:
                print("\nCreating ", newDir, "\n")
                os.mkdir(newDir)

            # Move silent files into newDir ("silentTemp")
            print("Moving silent files moved to ", newDir, "\n")
            for file in silentWavs:
                source = os.path.join(sourceDir, file)
                dest = os.path.join(newDir, file)
                shutil.move(source, dest)
            print("Moved silent files to ", newDir, "\n")

        else:
            print("\nIncorrect input. Files not Moved. Exiting...")
            exit()

# Prompt for creation of .zip archive of files
print("\nWould you like to create a zip archive of files?")
print("Original files and folders will be preserved")
print(".zip will include silent files if they were not removed")
zipAnswer = input("Type (Y)es or (N)o and press enter\n").upper()
# If user answers no, do nothing
if zipAnswer[0] == "N":
    print("\nNo archive created.\nExiting...")
    exit()

# If yes, create new folder, copy files to new folder,
# and create a zip of the folder.
if zipAnswer[0] == "Y":
    zipName = os.getcwd()
    # Check if zip file already exists
    zipCheck = zipName + ".zip"
    if os.path.exists(zipCheck):
        print("\n", zipCheck, "file already exists")
        print("Would you like to overwrite\n", zipCheck, "?")
        checkAns = input("Enter (Y)es or (N)o\n").upper()
        if checkAns[0] == "N":
            print("Not overwriting file.\nExiting...")
            exit()
        elif checkAns[0] == "Y":
            print("\nOverwriting ", zipCheck)
        else:
            print("Improper input. File not over-written.\nExiting...")
            exit()

    baseDir = os.path.relpath(zipName)
    rootDir = os.path.relpath(zipName)
    print("Creating Zip Archive...")
    shutil.make_archive(zipName, 'zip', root_dir=rootDir, base_dir=baseDir)
    print("Zip archive of", zipName, "finished.\nExiting...")
    exit()
    