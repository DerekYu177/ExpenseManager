from DataFileManager import data_file_helper, photo_file_finder, persistor
from PhotoAnalyzer import image_processor
from UI import user_interface

from shared import *
from image_data import ImageData

import debug as global_debug

def begin():
    global_debug.set_debug(True)
    initialize_files()

    p = persistor.Persistor(False)

    photos_names = photo_file_finder.find_photos()

    for photo_name in photos_names:
        image_data = image_processor.image_data_from_image(photo_name)

        p.protected_t_append(image_data)

def initialize_files():
    GlobalVariables.RECEIPT_LOCATION = image_file_when_debugging()

def image_file_when_debugging():
    if not global_debug.DebugCore.GLOBAL_DEBUG:
        return user_interface.prompt_user_for_location()

    return GlobalVariables.IMAGE_LOCATION
