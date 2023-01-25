import csv
import shutil
import os
import glob
from PIL import Image


# name of each SKU in the excel file
skus = []

# input path directory
def main():
    excel_file = input("excel_file> ").replace('"', "")
    path1 = input("path1> ").replace("\\", "\\\\")
    path2 = input("path2 ").replace("\\", "\\\\")

    # calls the search skus
    search_skus(excel_file)
    # calls the copy and paste images
    copy_images(path1, path2)
    # add stamp to the images
    add_stamp(path2)


# search for SKUs in the excel file and append to the [skus list]
def search_skus(excel):

    with open(excel) as file:
        reader = csv.DictReader(file)
        for row in reader:
            skus.append({"SKU": row["SKU"], "ID": row["ID"]})


# copy each SKU from the skus list in a specific folder and place it to another folder
def copy_images(p1, p2):
    for sku in skus:
        print(f'{sku["SKU"]}.jpg')
        # shutil.copyfile is used to copy from one folder to another
        original = f'{p1}\\{sku["SKU"]}.jpg'
        target = f'{p2}\\{sku["SKU"]}.jpg'
        shutil.copyfile(original, target)


# add an image stamp to each image copied to the new directory
def add_stamp(p2):
    for sku in skus:
        # open image in the directory specified by user
        image1 = Image.open(f'{p2}\\{sku["SKU"]}.jpg')
        # open the stamp image on a specif directory
        image2 = Image.open(
            "G:\\Meu Drive\\Projects_py\\CS50\\finalproject\\logo\\stamp.png"
        )
        # convert images to sepecifiz size 1000x1000 for images chosen by user and 50x50 the any stamp
        image1.thumbnail((1000, 1000))
        image2.thumbnail((50, 50))
        # paste the stamp in the image and save it
        image1.paste(image2, (0, 50))
        image1.save(f'{p2}\\{sku["SKU"]}.jpg')


if __name__ == "__main__":
    main()
