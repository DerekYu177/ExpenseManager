#!/usr/bin/python2.7

# built-in classes
import Modules.shared               as shared
import Modules.photo_file_finder    as photo_file_finder
import Modules.persistor            as persistor
import Modules.image_processor      as image_processor
import Modules.debug                as debug
import Modules.user_interface       as user_interface

def main():
    # print image_processor.text_from_image("grocery_store.jpg")

    # path = "%s/medium_def_receipt.jpg" % (shared.GlobalVariables.IMAGE_LOCATION)
    #
    # ui = user_interface.UserInterface()
    # ui.display_image(path)
    print photo_file_finder.all_photos_in_location()

main()

def execute():
    # access list of all photo files
    list_of_photos_files = photo_file_finder.all_photos_in_location()

    # iterate over all photos in list_of_photos_files
    for photo_file in list_of_photos_files:
        image_processor.text_from_image(photo_file)
