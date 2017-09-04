from enum import Enum
from collections import OrderedDict
import os

directory = os.getcwd()

class GlobalVariables:
    RECEIPT_LOCATION = ""
    IMAGE_LOCATION = '%s/test/images' % (directory)

class GlobalConstants:
    PYTESSERACT_LOCATION = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'
    PERSISTED_DATA = 'persisted_data.csv'
    PERSISTED_DATA_PATH = '%s/data/%s' % (directory, PERSISTED_DATA)
    TEST_PERSISTED_DATA_PATH = '%s/data/test_%s' % (directory, PERSISTED_DATA)

class BuilderRequirements(Enum):
    AS_IS = 0
    REQUIRES_ADDRESS = 1
    REQUIRES_DESCRIPTION = 2
    REQUIRES_COMPLETE = 3

class ImageDataCore:
    PROCESSED_ATTRIBUTES = [
        "date",
        "time",
        "total_amount"
    ]

    UNCERTAIN_ATTRIBUTES = [
        "address",
        "description"
    ]

    ANALYSIS_ATTRIBUTES = PROCESSED_ATTRIBUTES + UNCERTAIN_ATTRIBUTES

class ImageDataBuilder:
    PRECISION = BuilderRequirements.AS_IS

    BUILDER_ATTRIBUTES = OrderedDict([
        ("date_time", 0),
        ("address", 1),
        ("total_amount", 0),
        ("description", 2)
    ])
