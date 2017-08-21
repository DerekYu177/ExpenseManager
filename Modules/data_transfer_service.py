from DataFileManager import data_file_helper, photo_file_finder, persistor
from PhotoAnalyzer import image_processor
from UI import user_interface

from shared import *
from image_data import ImageData

from debug import BaseDebug
from debug import DebugCore
from debug import DebugState

class DataTransferService:
    DEBUG_STATE = True
    PERSISTANCE_STATE = DebugState.BASIC

    def __init__(self):
        BaseDebug().set_debug(self.DEBUG_STATE)
        GlobalVariables.RECEIPT_LOCATION = self._image_file()
        self.p = persistor.Persistor(self.PERSISTANCE_STATE)
        self.photos_names = photo_file_finder.find_photos()

    def begin(self):
        for photo_name in self.photos_names:
            image_data = image_processor.image_data_from_image(photo_name)
            self.p.protected_t_append(image_data)

    def _image_file(self):
        if DebugCore.GLOBAL_DEBUG.value > 0:
            return user_interface.prompt_user_for_location()

        return GlobalVariables.IMAGE_LOCATION
