# Grabbing current directory
import os

class global_variables:
    CURRENT_DIRECTORY = os.getcwd()

    IMAGE_LOCATION = '%s/../Test/Images' % (CURRENT_DIRECTORY)

    RECEIPT_LOCATION = ""

    DEBUG = False

class global_constants:
    PYTESSERACT_LOCATION = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'
