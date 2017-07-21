from shared import GlobalVariables
import user_interface

# for retrieving all files in directory
from os import listdir
from os.path import isfile

# to determine if a valid photo
import re

def all_photos_in_location():
    GlobalVariables.RECEIPT_LOCATION = user_interface.prompt_user_for_location()

    photos = PhotoFileFinder().find_photos()

    return photos

class PhotoFileFinder:

    def __init__(self):
        pass

    def find_photos(self):
        if not GlobalVariables.RECEIPT_LOCATION:
            raise EnvironmentError('Receipt location not initialized')

        photos = []
        for photo in listdir(GlobalVariables.RECEIPT_LOCATION):
            if self.is_photo(photo):
                photos.append(photo)

        if GlobalVariables.DEBUG:
            self.__debug_print_all_photo_files_in_location(photos)

        return photos

    def is_photo(self, photo_name):
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

    def print_list_to_string(self, item_list):
        string = ""

        if type(item_list) is list:
            for item in item_list:
                string = string + item + "\n"
        else:
            string = item_list

        return string

    def __debug_print_all_photo_files_in_location(observed_photos):
        print "All the photo files located in the receipt location %s are %s" % (
         GlobalVariables.RECEIPT_LOCATION, self.print_list_to_string(observed_photos)
        )