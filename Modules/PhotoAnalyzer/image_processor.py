from PIL import Image as img
import pytesseract
import re
import sys

from ..shared         import GlobalVariables
from ..shared         import GlobalConstants
from ..image_data     import ImageData, Core
from ..debug          import ImageTextSearch as debug

# set the path to the tesseract package
pytesseract.pytesseract.tesseract_cmd = GlobalConstants.PYTESSERACT_LOCATION

# open the debug class
debug = debug()

def image_data_from_image(image):
    image_location = GlobalVariables.IMAGE_LOCATION + "/" + image

    text = pytesseract.image_to_string(
        img.open(image_location)
    )

    its = ImageTextSearch(text)

    if its.is_photo:
        return its.analyze()

    return None

class ImageTextSearch:

    def __init__(self, original_text):
        self.original_text = original_text
        self.core_data = None
        self.is_photo = self.is_photo_receipt()

    # Public Facing

    def is_photo_receipt(self):
        empty_core_data = dict.fromkeys(Core.ANALYSIS_ATTRIBUTES, None)
        self.core_data = self.populate_core_data(empty_core_data)

        for attr in Core.ANALYSIS_ATTRIBUTES:
            if (attr in Core.PROCESSED_ATTRIBUTES) and (self.core_data[attr] is None):
                return False

        if debug.LOCAL_DEBUG:
            debug.all_set_attributes(self)

        return True

    def populate_core_data(self, empty_core_data):
        for attr in Core.ANALYSIS_ATTRIBUTES:
            find_function = getattr(
                self,
                self._define_finders(attr)
            )
            value = find_function()

            if debug.LOCAL_DEBUG:
                debug.show_set_attributes(attr, value)

            empty_core_data[attr] = value

        return empty_core_data

    def analyze(self):
        if debug.LOCAL_DEBUG:
            debug.text_and_relevant_text(self.original_text, self.core_data)
            self.core_data.update(debug.append_original_text(self.core_data))

        return ImageData(self.core_data)

    # Finders

    def _define_finders(self, attr):
        return "_find_%s" % (attr)

    def _find_date(self):
        date_regex = r'(\d+/\d+/\d+)'
        return self._search(date_regex)

    def _find_time(self):
        time_regex = r'(\d+:\d+:\d+)'
        return self._search(time_regex)

    def _find_address(self):
        return None # TODO

    def _find_total_amount(self):
        money_regex = r'[$]\s*\d+\.\d{2}'
        amounts = self._search(money_regex)
        return self._max_amounts(amounts)

    def _find_description(self):
        return None # TODO

    # Helpers

    def _max_amounts(self, money_list):
        if money_list is None:
            return money_list

        if type(money_list) is str:
            return money_list

        if type(money_list) is list:
            return self._max_list_finder(money_list)

    def _max_list_finder(self, money_list):
        max_amount = 0

        for money in money_list:
            m = self._strip_dollar_sign(money)

            if m > max_amount:
                max_amount = m

        return self._add_dollar_sign(max_amount)

    def _strip_dollar_sign(self, money):
        if money[0] != "$":
            return

        return float(money[1:])

    def _add_dollar_sign(self, number):
        number = str(number)

        number = self._add_lost_zero(number)

        return "$" + number

    def _add_lost_zero(self, number):
        dollar, cents = number.split('.')

        if len(cents) == 0:
            return number + "00"
        elif len(cents) == 1:
            return number + "0"
        else:
            return number

    def _search(self, regex):
        match = re.findall(regex, self.original_text)

        if not match:
            return None

        if len(match) == 1:
            return match[0]

        return match
