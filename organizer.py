import os
import re
import sys
import shutil

def moveFileToDest(ext, sourcePath, destinyPath):
    for files in os.listdir("./Downloads"):
        if ext in files:
            shutil.move("./Downloads/"+files, "./Downloads/Organizer/"+ext+"/"+files)
            print(files+"moved")
def getAllExt():

    ext_list = []
    for files in os.listdir("./Downloads"):
        extension = os.path.splitext(files)[1]
        if not extension in ext_list:
            if not extension == '':
                ext_list.append(extension)

    return ext_list


def main():
    if not os.path.exists("./Downloads/Organizer"):
        os.mkdir('./Downloads/Organizer')
        print("Organizer folder created")

    else:
        print("Starting...")
        extension_list = getAllExt()
        print(extension_list)
        for ext in extension_list:
            print("./Downloads/Organizer/"+ext)
            if not os.path.exists("./Downloads/Organizer/"+ext):
                os.mkdir("./Downloads/Organizer/"+ext)
                print("./Downloads/Organizer/"+ext)
            else:
                print(ext+"folder already created")

        for ext in extension_list:
           moveFileToDest(ext,"./Downloads","./Downloads/Organizer/"+ext)


main()


