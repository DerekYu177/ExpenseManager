#!/usr/bin/python2.7

# build in classes
import Modules.shared as shared
import Modules.file_accessor as file_accessor
import Modules.persistor as persistor
import Modules.image_processor as image_processor
import Modules.debug as debug

def main():



    print image_processor.text_from_image("medium_def_receipt.jpg")
    # debug.show_sys_path()

main()


def execute():
    # access list of all photo files
    list_of_photos_files = file_accessor.all_photos_in_location()
    #
    for photo_file in list_of_photos_files:
        image_processor.text_from_image(photo_file)
