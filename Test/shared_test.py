import unittest
import pytest
from ..Modules import shared as shared

class TestMethods(unittest.TestCase):
    def test_global_variables(self):
        assert shared.global_variables.RECEIPT_LOCATION == ""
        assert shared.global_variables.IMAGE_LOCATION

        # we don't test to allow DEBUG to function in tests
        # assert shared.global_variables.DEBUG == False

    def test_global_constants(self):
        assert shared.global_constants.PYTESSERACT_LOCATION
        assert shared.global_constants.PERSISTED_DATA
        assert shared.global_constants.PERSISTED_DATA_PATH
