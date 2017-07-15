from shared import global_variables as global_variables
from shared import global_constants as global_constants

# required for image processing
from PIL import Image as img
from PIL import ImageEnhance as img_enhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = shared.global_constants.PYTESSERACT_LOCATION

# required for text analysis
import re

def text_from_image(image):
    image_location = shared.global_variables.IMAGE_LOCATION + "/" + image

    text = pytesseract.image_to_string(
        img.open(image_location)
    )

    s = ImageText(text)

    return s.relevant_text()

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

class ImageText:

    def __init__(self, text):
        self.text = text

    def relevant_text(self):
        relevant_text = {}
        relevant_text.update(self.find_datetime())
        relevant_text.update(self.find_total_amount())

        if global_variables.DEBUG:
            self.__debug_text_and_relevant_text(relevant_text)
            relevant_text = self.__debug_append_original_text(relevant_text)

        return relevant_text

    def find_address(self):
        raise NotImplementedError

    def find_total_amount(self):
        money_regex = r'[$]\s*\d+\.\d{2}'

        amounts = re.findall(money_regex, self.text)
        amount = self.__max_amounts(amounts)

        total_amount = {
            "total_amount": amount,
        }

        return total_amount

    def find_datetime(self):
        date_regex = r'(\d+/\d+/\d+)'
        time_regex = r'(\d+:\d+:\d+)'

        date = self.__search_singular_with_regex(date_regex)
        time = self.__search_singular_with_regex(time_regex)

        date_time = {
            "date": date,
            "time": time
        }

        return date_time

    def __max_amounts(self, money_list):
        max_amount = 0

        for money in money_list:
            m = self.__strip_dollar_sign(money)

            if m > max_amount:
                max_amount = m

        return self.__add_dollar_sign(max_amount)

    def __strip_dollar_sign(self, money):
        if money[0] == "$":
            return float(money[1:])

    def __add_dollar_sign(self, number):
        number = str(number)

        number = self.__add_lost_zero(number)

        return "$" + number

    def __add_lost_zero(self, number):
        dollar, cents = number.split('.')

        if len(cents) == 0:
            return number + "00"
        elif len(cents) == 1:
            return number + "0"
        else:
            return number

    def __search_singular_with_regex(self, regex):
        match = re.search(regex, self.text)

        if match is None:
            return None
        else:
            return match.group()

    def __debug_text_and_relevant_text(self, relevant_text):
        print "The original text was : %s" % (self.text)
        print "The relevant text was : %s" % (relevant_text)

    def __debug_append_original_text(self, relevant):
        return {
            "original text": self.text,
            "relevant text": relevant
        }
