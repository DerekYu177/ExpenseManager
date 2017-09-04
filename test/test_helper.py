from ..modules import shared
from ..modules import debug

# @classmethod
# def setup_class(cls):
#     test_helper.prepare()

def prepare():
    shared.GlobalVariables.DATA_PATH = shared.GlobalConstants.TEST_PERSISTED_DATA_PATH
    debug.DebugCore.GLOBAL_DEBUG = debug.DebugState.BASIC
    shared.GlobalVariables.RECEIPT_LOCATION = shared.GlobalVariables.IMAGE_LOCATION

class TestHelper(object):
    @classmethod
    def setup_class(cls):
        prepare()
