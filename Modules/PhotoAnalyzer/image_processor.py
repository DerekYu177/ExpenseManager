from PIL import Image as img
import pytesseract

from ..shared         import GlobalVariables
from ..shared         import GlobalConstants
from ..shared         import ImageDataCore
from ..image_data     import ImageData
from ..debug          import DebugImageProcessor as debug
from finder           import Finder

# set the path to the tesseract package
pytesseract.pytesseract.tesseract_cmd = GlobalConstants.PYTESSERACT_LOCATION

# open the debug class
debug = debug()

def image_data_from_image(image):
    image_location = GlobalVariables.IMAGE_LOCATION + "/" + image

    if debug.LOCAL_DEBUG:
        debug.show_image_name(image_location)

    text = pytesseract.image_to_string(
        img.open(image_location)
    )

    return ImageTextSearch(text).analyze()

class ImageTextSearch:
    def __init__(self, original_text):
        self.original_text = original_text
        self.core_data = dict.fromkeys(ImageDataCore.ANALYSIS_ATTRIBUTES, None)
        self._populate_core_data()

    def analyze(self):
        if debug.LOCAL_DEBUG:
            debug.text_and_relevant_text(self.original_text, self.core_data)
            self.core_data.update(debug.append_original_text(self.core_data))

        return ImageData(self.core_data)

    def _populate_core_data(self):
        f = Finder(self.original_text)

        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            find_function = getattr(f, f.define_finders(attr))
            value = find_function()
            self.core_data[attr] = value

        if debug.LOCAL_DEBUG:
            debug.show_full_data(self.core_data)
