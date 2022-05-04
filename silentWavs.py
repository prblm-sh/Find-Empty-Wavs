import sox
import os
import shutil

# Get user input for working directory
path = input("Please enter directory path\nLeave empty and press enter to use current directory\n")

# If no input, use current directory
if len(path) <= 0:
    workDir = os.path.abspath(os.getcwd())
else:
    workDir = os.path.abspath(path)
    os.chdir(workDir)

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


# Empty list for files with sound
loudWavs = []
# Empty list for SILENT Files
silentWavs = []

# for every file in wavList, check if silent
# 2nd arg in silent() is threashold for 
# determining silence. Set so that a track
# with ANY amplitude AT ALL will not be touched
for wav in wavList:
    if sox.file_info.silent(wav, 0.0000000000000001):
        silentWavs.append(wav)
        print(wav, "is silent")

# If no .wav files are found, notify user and exit
if len(wavList) == 0:
    print("No .wav files found in ", workDir, "\nExiting.")
    exit()

# If no silent .wav files are found, notify user and exit
if len(silentWavs) == 0:
    print("No SILENT .wav files found. Exiting\n")
    exit()

numOfSilentWavs = len(silentWavs)
print(numOfSilentWavs, "silent files in", workDir, "\n")

# Prints various stats about silent .wav files
# Amp values should be 0.0 silent files
print("Verify .wav files are silent")
print("Amplitude values should be 0.0\n")

for x in silentWavs:
    stat = sox.file_info.stat(x)
    print(x, stat, "\n")

# Prompt for moving silent files to new directory
# to separate them from LOUD files for verification
print("Would you like to move ", numOfSilentWavs, " silent files to a separate directory?")
movAnswer = input("Type (Y)es or (N)o and press enter\n").upper()

# Declare directory vars outside of move loop
# so they can be used in delete loop
sourceDir = workDir
tempDir = "silentTemp"
newDir = os.path.join(sourceDir, tempDir)

# If No, leave files in original directory
if movAnswer[0] == "N":
    print("\nLeaving files in place.\n")

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
    print("Moved silent files to ", newDir)

else:
    print("Incorrect input. Exiting.")
    exit()

# prompt for deletion of silent files
print("\nWould you like to remove ", numOfSilentWavs, " silent .wav files?")
delAnswer = input("Enter (y)es or (n)o and press enter\n").upper()

# If user answers No, don't touch files and exit
if delAnswer[0] == "N":
    print("\nNo files removed. If files were moved,")
    print("Run script again in silentTemp directory")
    print("if you want to remove silent .wavs")
    print("Exiting...\n")
    exit()

# If user answers yes
elif delAnswer[0] == "Y":
    # If files were */NOT/* moved, delete from current dir
    if movAnswer[0] == "N":
        print(numOfSilentWavs, "\nSilent .wav files will be removed")
        for w in silentWavs:
            os.remove(w)
            print(w, "removed")
        print("Silent files removed. Exiting...")

    # If files */WERE/* moved, delete
    # from created temp dir, then 
    # delete temp dir
    elif movAnswer[0] == "Y":
        os.chdir(newDir)
        tempFiles = os.listdir()
        print(numOfSilentWavs, " silent .wav files will be removed")
        for tmp in tempFiles:
            print(tmp, " removed")
            os.remove(tmp)
        os.chdir(sourceDir)
        os.rmdir(newDir)
        print("removing silentTemp directory")
        print("Done. Exiting...")

else:
    print("Incorrect input. Exiting.")
    exit()