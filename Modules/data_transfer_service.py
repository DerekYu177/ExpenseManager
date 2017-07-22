from DataManager import persistor
from FileManager import data_file_helper, photo_file_finder
from PhotoAnalyzer import image_processor
from UI import user_interface

from shared import *
from image_data import *

def begin():
    initialize_files()

    p = persistor.Persistor()

    photos_names = photo_file_finder.get_photo_names()

    for photo_name in photos_names:
        image_data = image_processor.image_data_from_image(photo_name)

        if not p.does_data_exist(image_data):
            p.persist_data(image_data)

def initialize_files():
    GlobalVariables.RECEIPT_LOCATION = user_interface.prompt_user_for_location()

    file_helper = data_file_helper.DataFileHelper()
    file_helper.initialize_data_file
