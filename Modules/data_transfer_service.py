from DataManager import *
from FileManager import *
from PhotoAnalyzer import *
from UI import *

from shared import *
from image_data import *

def begin():
    GlobalVariables.RECEIPT_LOCATION = UI.user_interface.prompt_user_for_location()

    # TODO: here
