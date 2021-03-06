from PIL import Image as img
import pytesseract

from ..shared         import GlobalVariables
from ..shared         import GlobalConstants
from ..image_data     import Attributes
from ..image_data     import ImageData
from ..debug          import DebugImageProcessor as debug
from finder           import Finder

# set the path to the tesseract package
pytesseract.pytesseract.tesseract_cmd = GlobalConstants.PYTESSERACT_LOCATION

# open the debug class
debug = debug()

def image_data_from_image(image):
    image_location = GlobalVariables.IMAGE_LOCATION + "/" + image

    debug.show_image_name(image_location)

    text = pytesseract.image_to_string(
        img.open(image_location)
    )

    return ImageTextSearch(text, image).analyze()

class ImageTextSearch:
    def __init__(self, original_text, image_name):
        self.original_text = original_text
        self.image_name = image_name
        self.core_data = dict.fromkeys(Attributes.ANALYSIS_ATTRIBUTES, None)
        self._populate_core_data()

    def analyze(self):
        debug.text_and_relevant_text(self.original_text, self.core_data)
        self.core_data.update(debug.append_original_text(self.core_data))

        return ImageData(self.core_data, self.image_name)

    def _populate_core_data(self):
        f = Finder(self.original_text)

        for attr in Attributes.ANALYSIS_ATTRIBUTES:
            find_function = getattr(f, f.define_finders(attr))
            value = find_function()
            self.core_data[attr] = value

        debug.show_full_data(self.core_data)
