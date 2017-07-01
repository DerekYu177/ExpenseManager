from shared import global_variables

# for file prompt
from Tkinter import Tk
from tkFileDialog import askdirectory

# for retrieving all files in directory
from os import listdir
from os.path import isfile

# to determine if a valid photo
import re

def all_photos_in_location():
    global_variables.RECEIPT_LOCATION = prompt_user_for_location()

    photos = find_photos()

    if global_variables.DEBUG:
        print "All the files located in the receipt location %s are %s" % (
         global_variables.RECEIPT_LOCATION, print_list_to_string(photos)
        )

    return photos

def find_photos():
    if not global_variables.RECEIPT_LOCATION:
        raise EnvironmentError('Receipt location not initialized')

    photos = []
    for photo in listdir(global_variables.RECEIPT_LOCATION):
        if is_photo(photo):
            photos.append(photo)

    return photos

def is_photo(photo_name):
    if not type(photo_name) is str:
        return False

    accepted_file_formats = [
        ".jpg",
        ".png",
        ".jpeg",
    ]

    for file_format in accepted_file_formats:
        if re.search(re.compile(file_format), photo_name):
            return True

    return False

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
