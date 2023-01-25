import csv
import shutil
from PIL import Image
import glob
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Search for SKUs, and apply heroshot stamp")
parser.add_argument("-e", help="enter the CSV file", type=str)
parser.add_argument("-m", help=" enter the main location path", type=str)
parser.add_argument("-f", help="enter the final location", type=str)
args = parser.parse_args()


class Sku:
    
    

    # input path directory
    def __init__(self, excel_file, path1, path2):
        self.excel_file = excel_file
        self.path1 = path1
        self.path2 = path2
        self.sku_list = [] # store the name of each SKU in the excel file

    # search for SKUs in the excel file and append to the [skus list]
    def search_skus(self):
        try:
            # user must upload an CSV otherwise it wont work
            if ".csv" not in self.excel_file:
                print("******You need to upload an CSV file******")
            else:
                with open(self.excel_file) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        self.sku_list.append({"SKU": row["SKU"], "ID": row["ID"]})      
        
        # into the CSV must have a colum called SKU
        except KeyError:
            print("******The excel file must have a SKU colum*******")

    # copy each SKU from the skus list in a specific folder and place it to another folder
    def copy_images(self):
        for sku in self.sku_list:
            try:
                print(f'{sku["SKU"]}.jpg')
                # shutil.copyfile is used to copy from one folder to another
                original = glob.glob(f'{self.path1}\\**\\{sku["SKU"]}.jpg')
                target = f'{self.path2}\\{sku["SKU"]}.jpg'
                shutil.copyfile(original[0], target)
            # in case there is no such file in the folder, the program is going to skip and move to the next file
            except IndexError:
                pass

    # add an image stamp to each image copied to the new directory
    def add_stamp(self):
        for sku in self.sku_list:                         
            try:
                image1 = Image.open(f'{self.path2}\\{sku["SKU"]}.jpg')
                # open the stamp image on a specif directory
                image2 = Image.open("stamp.png")            
                # convert images to a sepecific size 1000x1000 for images chosen by user and 100x100 the any stamp
                image1.thumbnail((1000, 1000))
                image2.thumbnail((100, 100))
                # paste the stamp in the image and save it
                image1.paste(image2, (0, 50))
                image1.save(f'{self.path2}\\{sku["SKU"]}.jpg')
            # stamp.png file must be in the right folder C:\temp\heroshot
            except (FileNotFoundError, UnboundLocalError):           
                sys.exit
                print("stamp.png is not in the folder C:\temp\heroshot")            
                                    
def main():
        
    skus = Sku(args.e, args.m, args.f)
    # calls the search skus
    skus.search_skus()
    # calls the copy and paste images
    skus.copy_images()
    # add stamp to the images
    skus.add_stamp()

'''
def main():
    while True:
        # input path directory
        excel_file = input("excel_file> ").replace('"', "")
        path1 = input("path1> ").replace("\\", "\\\\")
        path2 = input("path2> ").replace("\\", "\\\\")

        skus = Sku(excel_file, path1, path2)
        # calls the search skus
        skus.search_skus()
        # calls the copy and paste images
        skus.copy_images()
        # add stamp to the images
        skus.add_stamp()
'''

if __name__ == "__main__":
    main()

main()
