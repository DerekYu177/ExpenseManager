import unittest, pytest
from ..modules.shared import GlobalConstants
from ..modules.shared import GlobalVariables
from ..modules.image_data import ImageData


class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global test_data, image_data

        image_data = ImageData({
            "date": "07/01/17",
            "time": "20:48:14",
            "address": "None",
            "total_amount": "$2017.21",
            "description": "test data"
        })

    def test_initializa(self):
        assert image_data

    def test_as_csv_text(self):
        expected = "070117-20:48:14,None,$2017.21,test data"

        assert image_data.as_csv_text() == expected

    def test_identifier(self):
        expected = "070117-20:48:14"

        assert image_data.identifier() == expected
