from data_file_manager import data_file_helper
from data_file_manager import photo_file_finder
from data_file_manager import persistor
from photo_analyzer import image_processor
import prompter

import shared
from image_data import ImageData

class DataTransferService:
    PERSISTANCE_STATE = False
    shared.ImageDataBuilder.PRECISION = shared.BuilderRequirements.AS_IS

    def __init__(self):
        shared.Setter().set_state(shared.State.DEBUG_BASIC)
        shared.GlobalVariables.RECEIPT_LOCATION = self._image_file()
        self.p = persistor.Persistor(self.PERSISTANCE_STATE)
        self.photos_names = photo_file_finder.find_photos()

    def begin(self):
        for photo_name in self.photos_names:
            image_data = image_processor.image_data_from_image(photo_name)
            self.p.protected_append(image_data)

    def _image_file(self):
        if shared.GlobalVariables.STATE is shared.State.NOMINAL:
            return prompter.prompt_user_for_location()

        return shared.GlobalVariables.IMAGE_LOCATION
