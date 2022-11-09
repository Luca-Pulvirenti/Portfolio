import os
from PIL import Image
import numpy as np
import tabulate


def create_array_informations(path_images):

    im = Image.open(path_images)
    x = np.array(im)

    return x


def list_info_image(list_path_images):
    # I chose to use a list because it was better to print with the "tabulate" form.
    table = []

    # Iteration in the image directory
    for path_images in list_path_images:
        name_images = os.path.basename(path_images)
        name_clean = os.path.splitext(name_images)[0]
        # This function it is useful to convert an image to an array with the Numpy library.
        x = create_array_informations(path_images)
        tipology = np.shape(x)

        # Find the mean values (grayscale, R,G,B,ALPHA) for each image.
        if len(tipology) == 2:

            grayscale = np.mean(x)

            # I insert within the table the values I'm interested in.
            table.append([name_clean, tipology[0], tipology[1], grayscale, 0, 0, 0, 0])
        else:
            alpha = 0
            tupla_averages = np.mean(x, axis=(0, 1))

            if tipology[2] == 4:
                alpha = tupla_averages[3]

            R, G, B = tupla_averages[:3]

            # I insert within the table the values that I am interested in.
            table.append([name_clean, tipology[0], tipology[1], 0, R, G, B, alpha])

    return table


def printa_tabule(table):
    headers = ["name", "height", "width", "greyscale", "R", "G", "B", "ALPHA"]
    print(tabulate.tabulate(table, headers, tablefmt="fancy_rid",floatfmt='.2f'))


# INSERT Path of the location of the "files" directory
position_files= ""

directory_name = "images"
directory_images = os.path.join(position_files,directory_name)

# Creation of a database with all the information we need about an image:
# 1) Height of the image, in pixels
# 2) Width of the image, in pixels.
# 3) If the image is greyscale, I'm interested in the average of the values in greyscale then of the one color layer.
# 4) If the image is in color, I'm interested of the average of the values of each color layer
list_of_images = [os.path.join(directory_images, image) for image in os.listdir(directory_images)]

# Creating a database via table with the information we need for each image.
table = list_info_image(list_of_images)

# Print of the table with the information I was interested, using the tabulate library.
printa_tabule(table)
