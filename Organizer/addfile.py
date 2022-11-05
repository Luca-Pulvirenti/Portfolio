import os
from os import path 
import shutil
import csv
import argparse

def create_directory(path,directory_name):

    directory_dest = path + "/" + directory_name
    os.mkdir(directory_dest)

def create_dictionary_file(name_file,resource):

    dictionary_file={}

    resource_file = resource + "/" + name_file
    if path.isfile(resource_file) :
        size = path.getsize(resource_file)
        name_split = path.splitext(name_file)
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

def create_set_types(path_files):
    exist = False
    set_types = set()
    name_elements = os.listdir(path_files)
    name_files = list(name_elements)
    for name in name_elements: 
        if path.isdir(path_files + "/" + name):
            name_files.remove(name)
            set_types.add(name)
        elif name == "recap.csv":
            exist = True 

    return set_types,name_files,exist

def move_file(position_files,name_file):

    set_types,name_files, exist = create_set_types(position_files)

    dictionary_file = create_dictionary_file(name_file,position_files)
    directory = dictionary_file[name_file]["type"]

    if directory not in set_types:
            set_types.add(directory)
            create_directory(position_files,directory)
    
    resource = position_files + "/" + name_file
    dest_path = position_files + "/" + directory
    shutil.move(resource,dest_path)

    return dictionary_file

def recap(path_position,dictionary):

    name_path = path_position + "/" + "recap.csv"

    
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

    position_files= "" ## INSERT Path of the location of the "files" directory.
    informations_of_files = move_file(position_files,args.name_file)
    recap(position_files,informations_of_files)

if __name__ == "__main__":
    main()

