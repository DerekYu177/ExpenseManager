import unittest, pytest

from ..modules import shared
from ..modules import image_data
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
        assert image_data.ImageData(test_data, image_name)

    def test_str_with_precision_as_is_replaces_none_appropriately(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.AS_IS
        data = image_data.ImageData(test_data, image_name)
        expected = "070117,2048(14),%s,$2017.21,%s" % (image_data.ImageData.EMPTY, image_data.ImageData.EMPTY)
        assert str(data) == expected

    def test_str_with_precision_requires_address(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.REQUIRES_ADDRESS
        data = image_data.ImageData(test_data, image_name)
        expected = "070117,2048(14),%s,$2017.21,%s" % (Query.DEFAULT_MESSAGE, image_data.ImageData.EMPTY)
        assert str(data) == expected

    def test_str_with_precision_requires_description(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.REQUIRES_DESCRIPTION
        data = image_data.ImageData(test_data, image_name)
        expected = "070117,2048(14),%s,$2017.21,%s" % (image_data.ImageData.EMPTY, Query.DEFAULT_MESSAGE)
        assert str(data) == expected

    def test_str_with_precision_requires_complete(self):
        shared.GlobalVariables.PRECISION = shared.BuilderRequirements.REQUIRES_COMPLETE
        data = image_data.ImageData(test_data, image_name)
        expected = "070117,2048(14),%s,$2017.21,%s" % (Query.DEFAULT_MESSAGE, Query.DEFAULT_MESSAGE)
        assert str(data) == expected
