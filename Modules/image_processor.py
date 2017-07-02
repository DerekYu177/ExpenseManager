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

    if shared.global_variables.DEBUG:
        print text

    datetime = find_datetime(text)

    return text, datetime

def find_address(text):
    raise NotImplementedError

def find_datetime(text):
    date_regex = r'(\d+/\d+/\d+)'
    time_regex = r'(\d+:\d+:\d+)'

    date = search_with_regex(date_regex, text)
    time = search_with_regex(time_regex, text)

    date_time = {
        "date": date,
        "time": time
    }

    if shared.global_variables.DEBUG:
        print date_time

    return date_time

def search_with_regex(regex, text):
    match = re.search(regex, text)

    if match is None:
        return None
    else:
        return match.group()

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
