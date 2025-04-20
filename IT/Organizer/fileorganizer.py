import os 
from os import path 
import shutil
import csv


def files_and_directories(position_files):

    # List of the path of each element in the files directory
    absolute_paths = [
        os.path.join(position_files, filename)
        for filename in os.listdir(position_files)
    ]

    # List of the directories in the files directory
    directories = [path for path in absolute_paths if os.path.isdir(path)]

    # List of the files in the files directory
    files = [path for path in absolute_paths if os.path.isfile(path)]

    # I need to check if the "recap.csv" file have been created before
    exists = any(file.endswith(RECAP_FILENAME) for file in files)

    # If the "recap.csv" file was created we should remove from the list of files
    if exists:
        # Remove the recap file
        files = [path for path in absolute_paths if not path.endswith(RECAP_FILENAME)]


    return files, directories


def create_dictionary_files(files):
    dictionary_files={}

    for filepath in files:
        # File is like C:\Users\fra\Desktop\My Doc.docx
        # Filename is like My Doc.docx
        filename = os.path.basename(filepath)

        # Size in byte of the file
        file_size = os.path.getsize(filepath)

        # Extension of the file
        _, file_extension = os.path.splitext(filepath)

        # Check what type of file it is to put the file in the right directory
        if file_extension in PICTURE_EXTENSIONS:
            dictionary_files[filename] = {"type": "images", "size": file_size, "absolute_dir": filepath}
        elif file_extension in DOCS_EXTENSIONS:
            dictionary_files[filename] = {"type": "docs", "size": file_size, "absolute_dir": filepath}
        elif file_extension in AUDIO_EXTENSIONS:
            dictionary_files[filename] = {"type": "audio", "size": file_size, "absolute_dir": filepath}
        else:
            dictionary_files[filename] = {"type": "other", "size": file_size, "absolute_dir": filepath}

    return dictionary_files


def iteration_files(position_files):

    # - I need to create a list of directories already present in the files directory
    # in order to use this information later on the iteration_files function.
    # - I need to create a list of files for the same reason.
    files, directories = files_and_directories(position_files)

    # Creo un dizionario per abbinare ogni file al suo tipo (immagine, documento, audio).
    dictionary_files = create_dictionary_files(files)

    # I create a dictionary to match each file to its type (image, document, audio) and size.
    directories_name = [os.path.basename(name) for name in directories ]

    # Iteration of files
    for name,info in dictionary_files.items():
        print(f"{name} type:{info['type']} size:{info['size']}\n")

        # Check if the directory already exists.
        # If it does not exist, add the directory and move the files to the directory.
        if info["type"] not in directories_name:
            directories_name.append(info["type"])
            directory_dest = os.path.join(position_files, info["type"])
            os.mkdir(directory_dest)

        # move files to the right directory
        resource = info["absolute_dir"]
        dest_path = os.path.join(position_files, info["type"])
        shutil.move(resource,dest_path)
    
    return dictionary_files


def recap(path_position,dictionary):

    # Composing the path of the "recap.csv" file
    name_path = os.path.join(path_position, RECAP_FILENAME)

    # Checking if the file already exist in order to understand if i should write the Header or not
    if not os.path.exists(name_path):
        with open(name_path,'w', encoding="UTF8", newline="") as f:
            writer = csv.writer(f)

            # Header
            writer.writerow(["name","type","size(B)"])

    # Opening the "recap.csv" file in order to write informations
    with open(name_path, "a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for name,info in dictionary.items():
            name_clean = path.splitext(name)[0]

            # Files
            writer.writerow([name_clean, info["type"], str(info["size"])])


# INSERT Path of the location of the "files" directory
position_files= ""
RECAP_FILENAME = "recap.csv"
PICTURE_EXTENSIONS = [".jpg", ".png", ".jpeg"]
DOCS_EXTENSIONS = [".txt", ".odt", ".docx"]
AUDIO_EXTENSIONS = [".mp3"]


# Creating a class Error for raise the "EmptyDeirectoryError" error.
class EmptyDirectoryError(Exception):
    pass


try:
    # Create a database (type "dictionary") to memorazie all the data of the file I'm interested
    # with these characteristcs :
    # {"filename": {"type":"name directory", "size": "size of the file"}.
    informations_of_files = iteration_files(position_files)
except EmptyDirectoryError:
    print(f"The directory {position_files} is empty!")
else:
    recap(position_files, informations_of_files)
