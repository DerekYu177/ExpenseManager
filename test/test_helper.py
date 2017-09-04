from ..modules import shared

class TestHelper(object):
    @classmethod
    def setup_class(cls):
        shared.GlobalVariables.DATA_PATH = shared.GlobalConstants.TEST_PERSISTED_DATA_PATH
        shared.Setter().set_state(shared.State.DEBUG_BASIC)
        shared.GlobalVariables.RECEIPT_LOCATION = shared.GlobalVariables.IMAGE_LOCATION
