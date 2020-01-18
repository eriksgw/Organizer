import os
import re
import sys
import shutil

def moveFilesToDestiny(extensions_list, sourcePath, destinyPath):
    for ext in extensions_list:
        for files in os.listdir(sourcePath):
            sourcePathFile = sourcePath+'/'+files
            if ext in files:
                destinyPathFile = destinyPath+'/'+ext+'/'+files
                shutil.move(sourcePathFile, destinyPathFile)
                print(files+" moved")

def getAllExtensionsFrom(sourcePath):

    ext_list = []
    for files in os.listdir(sourcePath):
        extension = os.path.splitext(files)[1]
        if not extension in ext_list and extension != '':
            ext_list.append(extension)

    return ext_list

def createFolderExt(extensions_list, directoryOrganizer):
    for ext in extensions_list:
        directoryOrganizerExt = directoryOrganizer+'/'+ext
        if not os.path.exists(directoryOrganizerExt):
            os.mkdir(directoryOrganizerExt)
        else:
            print(ext+" folder already created")

def startOrganizerProcediments(directoryPath, directoryOrganizer):
     extensions_list = getAllExtensionsFrom(directoryPath)
     createFolderExt(extensions_list, directoryOrganizer)
     moveFilesToDestiny(extensions_list, directoryPath, directoryOrganizer)


def main():
    directoryPath = input('Insert your directory path:')
    directoryOrganizer = directoryPath+'/Organizer'
    if not os.path.exists(directoryOrganizer):
        os.mkdir(directoryOrganizer)
        print("Organizer folder created. Starting...")
        startOrganizerProcediments(directoryPath, directoryOrganizer)
    else:
        print("Starting...")
        startOrganizerProcediments(directoryPath, directoryOrganizer)


main()


