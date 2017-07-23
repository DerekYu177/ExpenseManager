import os

directory = os.getcwd()

class GlobalVariables:
    RECEIPT_LOCATION = ""

    IMAGE_LOCATION = '%s/Test/Images' % (directory)

class GlobalConstants:
    PYTESSERACT_LOCATION = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'

    PERSISTED_DATA = 'persisted_data.csv'

    PERSISTED_DATA_PATH = '%s/Data/%s' % (directory, PERSISTED_DATA)
