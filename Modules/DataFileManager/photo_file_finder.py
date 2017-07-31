from os         import listdir
from os.path    import isfile
import re

from ..shared   import GlobalVariables
from ..debug    import PhotoFileFinder as debug

debug = debug()

def get_photo_names():
    # we assume that GlobalVariables is already set
    return PhotoFileFinder().find_photos()

class PhotoFileFinder:

    def __init__(self):
        pass

    def find_photos(self):
        if not GlobalVariables.RECEIPT_LOCATION:
            raise EnvironmentError('Receipt location not initialized')

        photos = []
        for photo in listdir(GlobalVariables.RECEIPT_LOCATION):
            if self.is_photo(photo):
                photos.append(photo)

        if debug.LOCAL_DEBUG:
            debug.print_all_photo_files_in_location(photos)

        return photos

    def is_photo(self, photo_name):
        if not type(photo_name) is str:
            return False

        accepted_file_formats = [
            ".jpg",
            ".png",
            ".jpeg",
        ]

        for file_format in accepted_file_formats:
            if re.search(re.compile(file_format), photo_name):
                return True

        return False
