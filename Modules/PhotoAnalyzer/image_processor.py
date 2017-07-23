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

    def is_photo_receipt(self):
        self.datetime = self.find_datetime()
        self.address = self.find_address()
        self.total_amount = self.find_total_amount()
        self.description = self.description()

        for attr in PROCESSED_ATTRIBUTES:
            if not self._dict_[attr]:
                return False

        return True

    def analyze(self):
        empty_text = dict.fromkeys(self.ANALYSIS_ATTRIBUTES, None)

        relevant_text = self._set_relevant_text_attributes(empty_text)

        if LOCAL_DEBUG:
            self._debug_text_and_relevant_text(relevant_text)
            relevant_text.update(self._debug_append_original_text(relevant_text))

        return ImageData(relevant_text)

    def _set_relevant_text_attributes(attr_dict):
        # this just sets all values in attr_dict by calling
        # find_#{attr} on each one
        # and returning the result
        for attr in ANALYSIS_ATTRIBUTES:
            attr_dict[attr] = getattr(
                sys.modules[__name__],
                "_find_%s" %(attr)
            )

        return attr_dict

    def _find_date(self):
        date_regex = r'(\d+/\d+/\d+)'
        return self._search_singular_with_regex(date_regex)

    def _find_datetime(self):
        time_regex = r'(\d+:\d+:\d+)'
        return = self._search_singular_with_regex(time_regex)

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

    def _debug_text_and_relevant_text(self, relevant_text):
        print "The original text was : %s" % (self.text)
        print "The relevant text was : %s" % (relevant_text)

    def _debug_append_original_text(self, relevant):
        return {
            "original text": self.text,
        }
