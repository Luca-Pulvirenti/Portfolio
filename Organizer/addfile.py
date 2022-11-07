import os
from os import path 
import shutil
import csv
import argparse

#Create a directory function
def create_directory(path,directory_name):

    directory_dest = path + "/" + directory_name
    os.mkdir(directory_dest)

# Create a database (type "dictionary") to memorazie all the data of the file I'm interested 
# with these characteristcs : 
# {"filename": {"type":"name directory", "size": "size of the file"}.
def create_dictionary_file(name_file,resource):

    dictionary_file={}

    resource_file = resource + "/" + name_file

    # Check to control if what we are analyzing it is a file.
    if path.isfile(resource_file) :
        size = path.getsize(resource_file)
        name_split = path.splitext(name_file)

        #Check what type of file it is to put the file in the right directory
        if name_split[1] == ".jpg" or name_split[1] == ".png" or name_split[1] == ".jpeg":
            dictionary_file[name_file]= {"type" : "images","size":size}
        elif name_split[1] == ".txt" or name_split[1] == ".odt" or name_split[1] == ".docx":
            dictionary_file[name_file]= {"type" : "docs","size":size}
        elif name_split[1] == ".mp3":
            dictionary_file[name_file]= {"type" : "audio","size":size}
        else:
            dictionary_file[name_file]= {"type" : "altro","size":size}
    else : 
        exit("the name you wrote doesn't identified a file")

    return dictionary_file

# I need to create a set to store all the directories already created.
# To not overwrite the macro directory with already existing directories.
def create_set_types(path_files):
    exist = False
    set_types = set()
    name_elements = os.listdir(path_files)
    name_files = list(name_elements)
    for name in name_elements: 
        if path.isdir(path_files + "/" + name):
            name_files.remove(name)
            set_types.add(name)

        # While i do this check it is usefull store if the "recap.csv" file it is already created.
        # In order to write a Hader ( we will do this in another part of the program) 
        # within the file if the file was not exist before.
        elif name == "recap.csv":
            exist = True 

    return set_types,exist

def move_file(position_files,name_file):
    # To check if the directory already exists, I create a set with the three categories (images, documents, audio).
    set_types, exist = create_set_types(position_files)

    # I create a dictionary to match the file to its type (image, document, audio) and size.
    dictionary_file = create_dictionary_file(name_file,position_files)

    # I acquire the directory name information.
    directory = dictionary_file[name_file]["type"]

    # Check the exist of the directory name.
    if directory not in set_types:
            set_types.add(directory)
            create_directory(position_files,directory)
    
    # move de file in the right directory.
    resource = position_files + "/" + name_file
    dest_path = position_files + "/" + directory
    shutil.move(resource,dest_path)

    return dictionary_file,exist
    
# Create a file CSV to recap all the file moved
def recap(path_position,dictionary,exist):

    name_path = path_position + "/" + "recap.csv"

    #Here is were we use the boolean "exist" the we made during the creating of the set().
    if not exist :
        with open(name_path,'w', encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            # Header
            writer.writerow(["name","type","size(B)"])
    
    with open(name_path,"a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for name,info in dictionary.items():
            name_clean = path.splitext(name)[0]
            #Files  
            writer.writerow([name_clean, info["type"], str(info["size"])])
            print("Il file è stato spostato con successo. Controlla il tuo recap !")

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("name_file", 
                        help= "I need the name of the file, like this 'file.jpg' ",
                        type= str)
    args = parser.parse_args()

    position_files= "/Users/lucas/OneDrive/Documenti/Python/Public_Projects/FileOrganizer/files" ## INSERIRE Path della posizione della directory "files".
    informations_of_files,exist = move_file(position_files,args.name_file)
    recap(position_files,informations_of_files,exist)

if __name__ == "__main__":
    main()

