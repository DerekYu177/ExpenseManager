#!/usr/bin/python2.7

# built-in classes
import Modules.shared               as shared
import Modules.photo_file_finder    as photo_file_finder
import Modules.persistor            as persistor
import Modules.image_processor      as image_processor
import Modules.debug                as debug
import Modules.user_interface       as user_interface
import Modules.data_file_helper     as data_file_helper

def main():

    # path = "%s/medium_def_receipt.jpg" % (shared.GlobalVariables.IMAGE_LOCATION)
    #
    # ui = user_interface.UserInterface()
    # ui.display_image(path)
    execute()

def execute():
    # access list of all photo files
    list_of_photos_files = photo_file_finder.all_photos_in_location()

    data_file_helper.DataFileHelper().initialize_data_file()

    p = persistor.Persistor()

    # iterate over all photos in list_of_photos_files
    for photo_file in list_of_photos_files:
        image_data = image_processor.image_data_from_image(photo_file)

        if not p.does_data_exist(image_data):
            p.persist(image_data)

if __name__ == '__main__':
    main()
