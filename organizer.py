import os
import re
import sys
import shutil

def moveFileToDest(ext, sourcePath, destinyPath):
    for files in os.listdir(sourcePath):
        sourcePathFile = sourcePath+'/'+files
        if ext in files:
            destinyPathFile = destinyPath+'/'+files
            shutil.move(sourcePathFile, destinyPathFile)
            print(files+" moved")

def getAllExt(sourcePath):

    ext_list = []
    for files in os.listdir(sourcePath):
        extension = os.path.splitext(files)[1]
        if not extension in ext_list:
            if not extension == '':
                ext_list.append(extension)

    return ext_list


def main():
    directoryPath = input('Insert your directory path:')
    directoryOrganizer = directoryPath+'/Organizer'
    if not os.path.exists(directoryPath):
        os.mkdir(directoryOrganizer)
        print("Organizer folder created")

    else:
        print("Starting...")
        extension_list = getAllExt(directoryPath)
        for ext in extension_list:
            directoryOrganizerExt = directoryOrganizer+'/'+ext
            if not os.path.exists(directoryOrganizerExt):
                os.mkdir(directoryOrganizerExt)
            else:
                print(ext+"folder already created")

        for ext in extension_list:
           moveFileToDest(ext,directoryPath,directoryOrganizerExt)


main()


