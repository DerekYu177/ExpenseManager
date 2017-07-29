from DataFileManager import data_file_helper, photo_file_finder, persistor
from PhotoAnalyzer import image_processor
from UI import user_interface

from shared import *
from image_data import ImageData

import debug

def begin():
    debug.set_debug(True)

    initialize_files()

    p = persistor.Persistor()

    photos_names = photo_file_finder.get_photo_names()

    for photo_name in photos_names:
        image_data = image_processor.image_data_from_image(photo_name)

        if image_data is not None:
            p.append(image_data)


def initialize_files():
    if debug.GLOBAL_DEBUG:
        GlobalVariables.RECEIPT_LOCATION = user_interface.prompt_user_for_location()
    else:
        GlobalVariables.RECEIPT_LOCATION = GlobalVariables.IMAGE_LOCATION

    data_file_helper.initialize_data_file()
