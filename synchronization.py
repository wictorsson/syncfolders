import os
import shutil
import time
from datetime import datetime

def SyncFolder(sourceFolder, replicaFolder, logfilePath):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
    sourceFiles = os.listdir(sourceFolder)
    replicaFiles = os.listdir(replicaFolder)
    logfile = open(logfilePath, 'a+')  
    #Add files
    for sourceFile in sourceFiles:
        sourceFilePath = os.path.join(sourceFolder, sourceFile)
        if sourceFile not in replicaFiles:
            shutil.copy2(sourceFilePath, replicaFolder)
            logMessage = f"Copy file: {sourceFile} to replica folder - {timestamp}"
            print(logMessage)
            logfile.write(logMessage + '\n')
    #Remove files
    for replicaFile in replicaFiles:
        if replicaFile not in sourceFiles:
            replicaPath = os.path.join(replicaFolder, replicaFile)
            os.remove(replicaPath)
            logMessage = f"Remove file: {replicaFile} from replica folder - {timestamp}"
            print(logMessage)
            logfile.write(logMessage + '\n')
    logfile.close()

def UserInput(param):
        if(param == "int"):
            while True:
                try:
                    return int(input("Enter interval in seconds: "))
                except ValueError:
                    print("Invalid input. Must be a whole number")
        elif(param == "source" or "replica" or "logfile"):
            while True:
                try:
                    displayString = "Enter " + param + " folder path: "
                    path = input(displayString)
                    if not os.path.exists(path):
                        print("Path of the", param, "is invalid")
                    else:
                        return path
                except ValueError:
                    print("An error occurred:")

def main():
    print("Welcome")
    syncInterval = UserInput("int")
    sourceFolder = UserInput("source")
    replicaFolder = UserInput("replica")
    logfileFolder = UserInput("logfile")
    logfilePath = os.path.join(logfileFolder, 'logfile.txt')

    while True:
        time.sleep(syncInterval)
        SyncFolder(sourceFolder, replicaFolder, logfilePath)

if __name__ == '__main__':
    main()


