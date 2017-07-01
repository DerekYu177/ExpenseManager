from shared import global_variables

# for file prompt
from Tkinter import Tk
from tkFileDialog import askdirectory

# for retrieving all files in directory
from os import listdir
from os.path import isfile

def all_images_in_location():
    # Returns a list of all the names of the photos in the RECEIPT_LOCATION

    global_variables.RECEIPT_LOCATION = prompt_user_for_location()

    photos = find_photos()

    if global_variables.DEBUG:
        print "All the files located in the receipt location %s are %s" % (
         global_variables.RECEIPT_LOCATION, print_list_to_string(photos)
        )

    return photos

def find_photos():
    if not global_variables.RECEIPT_LOCATION:
        raise NoReceiptLocationInstantiatedError

    photos = []
    for photo in listdir(global_variables.RECEIPT_LOCATION):
        if isfile(photo):
            photos.append(photo)

    return photos

def print_list_to_string(item_list):
    string = ""

    if type(item_list) is list:
        for item in item_list:
            string = string + item + "\n"
    else:
        string = item_list

    return string

def prompt_user_for_location():
    tk = Tk()
    tk.withdraw()

    return askdirectory()
