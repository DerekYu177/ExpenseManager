from enum import Enum
import os

directory = os.getcwd()

class State(Enum):
    NOMINAL = 0
    DEBUG_BASIC = 1
    DEBUG_VERBOSE = 2
    TEST = 3

class BuilderRequirements(Enum):
    AS_IS = 0
    REQUIRES_ADDRESS = 1
    REQUIRES_DESCRIPTION = 2
    REQUIRES_COMPLETE = 3

class GlobalConstants:
    PYTESSERACT_LOCATION = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'
    PERSISTED_DATA = 'persisted_data.csv'
    PERSISTED_DATA_PATH = '%s/data/%s' % (directory, PERSISTED_DATA)
    TEST_PERSISTED_DATA_PATH = '%s/data/test_%s' % (directory, PERSISTED_DATA)

class GlobalVariables: # FIXME: These can become module variables
    RECEIPT_LOCATION = ""
    IMAGE_LOCATION = '%s/test/images' % (directory)
    DATA_PATH = GlobalConstants.PERSISTED_DATA_PATH
    STATE = State.DEBUG_BASIC
    PRECISION = BuilderRequirements.AS_IS

class Setter:
    # TODO: the rest of the setters for access to key variables

    def set_state(self, new_state):
        if not new_state in State:
            return

        GlobalVariables.STATE = new_state
