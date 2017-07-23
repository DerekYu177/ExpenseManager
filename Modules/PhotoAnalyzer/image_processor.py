from PIL import Image as img
import pytesseract
import re
import sys

from ..shared         import GlobalVariables
from ..shared         import GlobalConstants
from ..image_data     import ImageData

# set the path to the tesseract package
pytesseract.pytesseract.tesseract_cmd = GlobalConstants.PYTESSERACT_LOCATION

# module level debug
LOCAL_DEBUG = False

def image_data_from_image(image):
    image_location = GlobalVariables.IMAGE_LOCATION + "/" + image

    text = pytesseract.image_to_string(
        img.open(image_location)
    )

    its = ImageTextSearch(text)

    if not its.is_photo:
        return

    return its.analyze()

#[Time, Location, Cost, Description]

class ImageTextSearch:
    ANALYSIS_ATTRIBUTES = [
        "date",
        "time",
        "address",
        "total_amount",
        "description"
    ]

    PROCESSED_ATTRIBUTES = [
        "date",
        "time",
        "total_amount"
    ]

    def __init__(self, text):
        self.text = text
        self.core_data = None
        self.is_photo = self.is_photo_receipt()

    # Public Facing

    def is_photo_receipt(self):
        empty_core_data = dict.fromkeys(self.ANALYSIS_ATTRIBUTES, None)
        self.core_data = self.populate_core_data(empty_core_data)

        for attr in self.ANALYSIS_ATTRIBUTES:
            if (attr in self.PROCESSED_ATTRIBUTES) and (self.core_data[attr] is None):
                return False

        if LOCAL_DEBUG:
            self._debug_all_set_attributes()

        self.core_data = empty_core_data
        return True

    def populate_core_data(self, empty_core_data):
        for attr in self.ANALYSIS_ATTRIBUTES:
            find_function = getattr(
                self,
                self._define_finders(attr)
            )
            value = find_function()
            empty_core_data[attr] = find_function()

        return empty_core_data

    def analyze(self):
        if LOCAL_DEBUG:
            self._debug_text_and_relevant_text(self.core_data)
            self.core_data.update(self._debug_append_original_text(self.core_data))

        return ImageData(self.core_data)

    # Finders

    def _define_finders(self, attr):
        return "_find_%s" % (attr)

    def _find_date(self):
        date_regex = r'(\d+/\d+/\d+)'
        return self._search_singular_with_regex(date_regex)

    def _find_time(self):
        time_regex = r'(\d+:\d+:\d+)'
        return self._search_singular_with_regex(time_regex)

    def _find_address(self):
        return None # TODO

    def _find_total_amount(self):
        money_regex = r'[$]\s*\d+\.\d{2}'

        amounts = re.findall(money_regex, self.text)

        if not amounts:
            return None

        return self._max_amounts(amounts)

    def _find_description(self):
        return None # TODO

    # Helpers

    def _max_amounts(self, money_list):
        max_amount = 0

        for money in money_list:
            m = self._strip_dollar_sign(money)

            if m > max_amount:
                max_amount = m

        return self._add_dollar_sign(max_amount)

    def _strip_dollar_sign(self, money):
        if money[0] == "$":
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

    def _search_singular_with_regex(self, regex):
        match = re.search(regex, self.text)

        if match is None:
            return None
        else:
            return match.group()

    # Debuggers

    def _debug_text_and_relevant_text(self, relevant_text):
        print "The original text was : %s" % (self.text)
        print "The relevant text was : %s" % (relevant_text)

    def _debug_append_original_text(self, relevant):
        return {
            "original text": self.text,
        }

    def _debug_all_set_attributes(self):
        for attr in ANALYSIS_ATTRIBUTES:
            print "%s has value %s" % (attr, self.__dict__[attr])
