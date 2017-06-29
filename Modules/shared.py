# Grabbing current directory
import os

directory = os.getcwd()

class global_variables:
    RECEIPT_LOCATION = "%s/../Receipts" % (directory)

    IMAGE_LOCATION = '%s/../Test/Images' % (directory)

    DEBUG = False

class global_constants:
    PYTESSERACT_LOCATION = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'

    PERSISTED_DATA = 'persisted_data.csv'

    PERSISTED_DATA_PATH = '%s/Data/%s' % (directory, PERSISTED_DATA)
