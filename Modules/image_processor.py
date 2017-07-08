import shared

# required for image processing
from PIL import Image as img
from PIL import ImageEnhance as img_enhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = shared.global_constants.PYTESSERACT_LOCATION

# required for text analysis
import re

def text_from_image(image):
    text = pytesseract.image_to_string(
        img.open(shared.global_variables.IMAGE_LOCATION + "/" + image)
    )

    s = SearchableText(text)

    datetime = s.find_datetime()
    total_amount = s.find_total_amount()

    return text, datetime


def enhance(image, enhance_factor, contrast_factor, sharpen_factor):
    # TODO: Does this even work?
    enhanced_image = img_enhance._Enhance(image)
    enhanced_image.enhance(enhance_factor)

    contrasted_image = img_enhance.Contrast(enhanced_image)
    contrasted_image.enhance(contrast_factor)

    sharpened_image = img_enhance.Sharpness(contrasted_image)
    sharpened_image.enhance(sharpen_factor)

    return sharpened_image

#[Time, Location, Cost, Description]

class SearchableText:

    def __init__(self, text):
        self.text = text

    # public facing methods

    def find_address(self):
        raise NotImplementedError

    def find_total_amount(self):
        money_regex = r'[$]\d+(?:\.\d{2})?'

        amounts = re.findall(money_regex, self.text)

        amount = self.max_amounts(amounts)

        total_amount = {
            "total_amount": self.add_dollar_sign(amount),
        }

        if shared.global_variables.DEBUG:
            print total_amount

        return total_amount

    def find_datetime(self):
        date_regex = r'(\d+/\d+/\d+)'
        time_regex = r'(\d+:\d+:\d+)'

        date = self.search_singular_with_regex(date_regex)
        time = self.search_singular_with_regex(time_regex)

        date_time = {
            "date": date,
            "time": time
        }

        if shared.global_variables.DEBUG:
            print date_time

        return date_time

    # private facing methods

    def max_amounts(self, money_list):
        max_amount = 0

        for money in money_list:

            m = self.strip_dollar_sign(money)

            if m > max_amount:
                max_amount = m

        return max_amount

    def strip_dollar_sign(self, money):
        if money[0] == "$":
            return float(money[1:])

    def add_dollar_sign(self, number):
        return "$%s" % (number)

    def search_singular_with_regex(self, regex):
        match = re.search(regex, self.text)

        if match is None:
            return None
        else:
            return match.group()
