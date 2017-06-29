# Grabbing current directory
import os

MODULE_DIRECTORY = os.getcwd()

class global_variables:
    RECEIPT_LOCATION = "%s/../Receipts" % (MODULE_DIRECTORY)

    IMAGE_LOCATION = '%s/../Test/Images' % (MODULE_DIRECTORY)

    DEBUG = False

class global_constants:
    PYTESSERACT_LOCATION = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'

    GLOBAL_DIRECTORY = '%s/..' % (MODULE_DIRECTORY)

    PERSISTED_DATA = 'persisted_data.csv'

    PERSISTED_DATA_PATH = '%s/Data/%s' % (GLOBAL_DIRECTORY, PERSISTED_DATA)
