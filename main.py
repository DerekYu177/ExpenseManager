#!/usr/bin/python2.7

# built-in classes
import Modules.shared               as shared
import Modules.file_accessor        as file_accessor
import Modules.persistor            as persistor
import Modules.image_processor      as image_processor
import Modules.debug                as debug
import Modules.user_interface       as user_interface

def main():
    # print image_processor.text_from_image("medium_def_receipt.jpg")

    path = "%s/medium_def_receipt.jpg" % (shared.global_variables.IMAGE_LOCATION)

    ui = user_interface.UserInterface(path)
    ui.display_image()


main()


def execute():
    # access list of all photo files
    list_of_photos_files = file_accessor.all_photos_in_location()
    #
    for photo_file in list_of_photos_files:
        image_processor.text_from_image(photo_file)
