#!/usr/bin/python2.7
import constants

# required for image processing
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = constants.PYTESSERACT_LOCATION

def main():
    print text_from_image("text_advanced.gif")

def text_from_image(image_name):
    return pytesseract.image_to_string(
        Image.open(constants.IMAGE_LOCATION + image_name)
    )

def debug():
    import sys
    for path in sys.path:
        print path

main()
