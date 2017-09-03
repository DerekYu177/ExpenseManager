from data_file_manager import data_file_helper
from data_file_manager import photo_file_finder
from data_file_manager import persistor
from photo_analyzer import image_processor
import prompter

from shared import ImageDataBuilder
from shared import BuilderRequirements
from shared import GlobalVariables
from image_data import ImageData

from debug import BaseDebug
from debug import DebugCore
from debug import DebugState

class DataTransferService:
    DEBUG_STATE = DebugState.BASIC
    PERSISTANCE_STATE = False
    ImageDataBuilder.PRECISION = BuilderRequirements.AS_IS

    def __init__(self):
        BaseDebug().set_debug(self.DEBUG_STATE)
        GlobalVariables.RECEIPT_LOCATION = self._image_file()
        self.p = persistor.Persistor(self.PERSISTANCE_STATE)
        self.photos_names = photo_file_finder.find_photos()

    def begin(self):
        for photo_name in self.photos_names:
            image_data = image_processor.image_data_from_image(photo_name)
            self.p.protected_append(image_data)

    def _image_file(self):
        if DebugCore.GLOBAL_DEBUG is DebugState.OFF:
            return prompter.prompt_user_for_location()

        return GlobalVariables.IMAGE_LOCATION
