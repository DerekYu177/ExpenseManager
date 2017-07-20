import unittest
import pytest
from ..Modules import shared as shared

class TestMethods(unittest.TestCase):
    def test_global_variables(self):
        assert shared.GlobalVariables.RECEIPT_LOCATION == ""
        assert shared.GlobalVariables.IMAGE_LOCATION

        # we don't test to allow DEBUG to function in tests
        # assert shared.GlobalVariables.DEBUG == False

    def test_global_constants(self):
        assert shared.GlobalConstants.PYTESSERACT_LOCATION
        assert shared.GlobalConstants.PERSISTED_DATA
        assert shared.GlobalConstants.PERSISTED_DATA_PATH
