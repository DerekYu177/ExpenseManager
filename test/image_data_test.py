import unittest, pytest

from ..modules import shared
from ..modules.image_data import ImageData
from ..modules.CLI import Query

class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global test_data, image_name
        shared.GlobalVariables.STATE = shared.State.TEST

        test_data = {
            "date": "07/01/17",
            "time": "20:48:14",
            "address": None,
            "total_amount": "$2017.21",
            "description": None
        }

        image_name = "dank_receipt.jpg"


    def test_initialize(self):
        assert ImageData(test_data, image_name)

    def test_str_with_precision_as_is(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.AS_IS
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,None,$2017.21,None"
        assert str(image_data) == expected

    def test_str_with_precision_requires_address(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.REQUIRES_ADDRESS
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,%s,$2017.21,None" % (Query.DEFAULT_MESSAGE)
        assert str(image_data) == expected

    def test_str_with_precision_requires_description(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.REQUIRES_DESCRIPTION
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,None,$2017.21,%s" % (Query.DEFAULT_MESSAGE)
        assert str(image_data) == expected

    def test_str_with_precision_requires_complete(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.REQUIRES_COMPLETE
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,%s,$2017.21,%s" % (Query.DEFAULT_MESSAGE, Query.DEFAULT_MESSAGE)
        assert str(image_data) == expected

    def test_identifier(self):
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14"
        assert image_data.identifier() == expected
