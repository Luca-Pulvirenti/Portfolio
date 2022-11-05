# 1 Trovare il percorso file della cartella "files" V
# 2 Iterare su ogni file all'interno della cartella "files" V
    # Ogni qual volta incontriamo un tipo di file non visto prima creare una sottocartella per quel tipo di file V 
    # Durante l'iterazione spostare ogni file nella cartella del corrispettivo tipo di file. V
# 3 Durante il ciclo lo script dovrà stampare le informazioni dei file: nome, tipo e dimensione in byte. V
# 4 Creare un file ( recap.csv ) che tenga traccia di tutti i file man mano che vengono spostati V

import os 
from os import path 
import shutil
import csv
import argparse

def positiondirectory():    #TODO
    pass

def create_directory(path,directory_name):
    
    directory_dest = path + "/" + directory_name
    os.mkdir(directory_dest)
    
def create_dictionary_files(name_file,resource):

    dictionary_files={}

    resource_file = resource + "/" + name_file
    if path.isfile(resource_file) :
        size = path.getsize(resource_file)
        name_split = path.splitext(name_file)
        if name_split[1] == ".jpg" or name_split[1] == ".png" or name_split[1] == ".jpeg":
            dictionary_files[name_file]= {"type" : "images","size":size}
        elif name_split[1] == ".txt" or name_split[1] == ".odt" or name_split[1] == ".docx":
            dictionary_files[name_file]= {"type" : "docs","size":size}
        else:
            dictionary_files[name_file]= {"type" : "audio","size":size}
    else : 
        exit("the name you wrote doesn't identified a file")

    return dictionary_files

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

def iteration_files(position_files,name_files1):

    # I create dictionary for match each files with their type (image,doc,audio)
    dictionary_files = create_dictionary_files(name_files1,position_files)

    #Iteration in the file
    for name,info in dictionary_files.items():
        # Check if the directory exist already
        #If not exist add the directory and move the files on the directory
        # move the files on the right directory
        resource = position_files + "/" + name
        dest_path = position_files + "/" + info["type"]
        shutil.move(resource,dest_path)

    return dictionary_files

def recap(path_position,dictionary):

    name_path = path_position + "/" + "recap.csv"

    
    with open(name_path,"a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for name,info in dictionary.items():
            name_clean = path.splitext(name)[0]
            #Files  
            writer.writerow([name_clean, info["type"], str(info["size"])])

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("name_file", 
                        help= "I need the name of the file, like this 'file.jpg' ",
                        type= str)
    args = parser.parse_args()

    position_files= "Insert the path of the directory that you want to 'organize'. "
    informations_of_files = iteration_files(position_files,args.name_file)
    recap(position_files,informations_of_files)

if __name__ == "__main__":
    main()

