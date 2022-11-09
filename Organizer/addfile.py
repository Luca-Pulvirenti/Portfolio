import os
from os import path 
import shutil
import csv
import argparse
import sys


def request_name_file(position_files):

    # Creation o the command line control
    parser = argparse.ArgumentParser()
    
    # Specification of the only mandatory topic
    parser.add_argument("name_file", help=" I need the name of the file, like this 'file.jpg' ", type=str)
    args = parser.parse_args()
    name_file = args.name_file
    
    # Creation of the file path
    path_file = os.path.join(position_files, name_file)

    return path_file


# Create a database (type "dictionary") to memorize all the data of the file I'm interested
# with these characteristics:
# {"filename": {"type":"name directory", "size": "size of the file"}.
def create_dictionary_file(path_file):

    dictionary_file = {}

    # I took the only file name
    name_file = os.path.basename(path_file)

    # I took the size in byte of the file
    size = path.getsize(path_file)

    # I took the extension of the file
    _, ext = path.splitext(name_file)

    # Check what type of file it is to put the file in the right directory
    if ext in IMAGE_EXTENSION:
        dictionary_file[name_file] = {"type": "images", "size": size}
    elif ext in DOC_EXTENSION:
        dictionary_file[name_file] = {"type": "docs", "size": size}
    elif ext in AUDIO_EXTENSION:
        dictionary_file[name_file] = {"type": "audio", "size": size}
    else:
        dictionary_file[name_file] = {"type": "altro", "size": size}

    return dictionary_file


def move_file(position_files, path_file):

    # I create a dictionary to match the file to its type (image, document, audio) and size.
    dictionary_file = create_dictionary_file(path_file)

    name_file = os.path.basename(path_file)

    # I acquire the directory name information.
    directory = dictionary_file[name_file]["type"]
    path_directory = os.path.join(position_files, directory)

    # Check the exist of the directory name.
    if not os.path.exists(path_directory):
        os.mkdir(path_directory)
    
    # move de file in the right directory.
    shutil.move(path_file, path_directory)

    return dictionary_file


# Creation of a file CSV to recap all the file moved
def recap(position_files, dictionary, name_recap):

    path_recap = os.path.join(position_files, name_recap)

    # Here is were we use the boolean "exist" the we made during the creating of the set().
    if not os.path.exists(path_recap):
        with open(path_recap, 'w', encoding="UTF8", newline="") as f:
            writer = csv.writer(f)

            # Header
            writer.writerow(["name", "type", "size(B)"])
    
    with open(path_recap, "a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for name, info in dictionary.items():
            name_clean = path.splitext(name)[0]

            # Files
            writer.writerow([name_clean, info["type"], str(info["size"])])
            print("Il file è stato spostato con successo. Controlla il tuo recap !")


# INSERT Path of the location of the "files" directory
position_files = ""
name_recap = "recap.csv"

IMAGE_EXTENSION = [".jpg", ".png", ".jpeg"]
DOC_EXTENSION = [".docx", ".txt", ".odt"]
AUDIO_EXTENSION = [".mp3"]

path_file = request_name_file(position_files)


# File existence check
if not os.path.exists(path_file):
    print(f'Il file <{os.path.basename(path_file)}> non esiste.')
    sys.exit(0)


# Moving the file to the correct folder
# Creation of a database with the information of the file i need
dictionary_file = move_file(position_files, path_file)

# Recap of moved files
recap(position_files, dictionary_file, name_recap)

