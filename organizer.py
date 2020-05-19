import os
import re
import sys
import shutil

def move_files_destiny(extensions, source_path, destiny_path):
    for ext in extensions:
        for files in os.listdir(source_path):
            source_path_file = source_path+'/'+files
            if ext in files:
                destiny_path_file = destiny_path+'/'+ext+'/'+files
                shutil.move(source_path_file, destiny_path_file)
                print(files+" moved")

def get_all_extension_from(source_path):
    ext_list = []
    for files in os.listdir(source_path):
        extension = os.path.splitext(files)[1]
        if extension not in ext_list and extension != '':
            ext_list.append(extension)

    return ext_list

def create_folder_ext(extensions, dir_organizer):
    for ext in extensions:
        directory_organizer_ext = dir_organizer+'/'+ext
        if not os.path.exists(directory_organizer_ext):
            os.mkdir(directory_organizer_ext)
        else:
            print(ext+" folder already created")

def start_organizer_procediments(dir_path, dir_organizer):
    extensions = get_all_extension_from(dir_path)
    create_folder_ext(extensions, dir_organizer)
    move_files_destiny(extensions, dir_path, dir_organizer)

def main():
    dir_path = input('Insert your directory path:')
    dir_organizer = dir_path+'/Organizer'
    if not os.path.exists(dir_organizer):
        os.mkdir(dir_organizer)
        print("Organizer folder created. Starting...")
        start_organizer_procediments(dir_path, dir_organizer)
    else:
        print("Starting...")
        start_organizer_procediments(dir_path, dir_organizer)
        
if __name__ == "__main__":
    main()


