import unittest, pytest
from ..modules.shared import GlobalConstants
from ..modules.shared import GlobalVariables
from ..modules.shared import ImageDataBuilder
from ..modules.shared import BuilderRequirements
from ..modules.image_data import ImageData
from ..modules.image_data import Builder

class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global test_data, image_name

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

    def test_as_csv_text_with_precision_as_is(self):
        ImageDataBuilder.PRECISION = BuilderRequirements.AS_IS
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,None,$2017.21,None"
        assert image_data.as_csv_text() == expected

    def test_as_csv_text_with_precision_requires_address(self):
        ImageDataBuilder.PRECISION = BuilderRequirements.REQUIRES_ADDRESS
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,%s,$2017.21,None" % (Builder.SUBSTITUTE)
        assert image_data.as_csv_text() == expected

    def test_as_csv_text_with_precision_requires_description(self):
        ImageDataBuilder.PRECISION = BuilderRequirements.REQUIRES_DESCRIPTION
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,None,$2017.21,%s" % (Builder.SUBSTITUTE)
        assert image_data.as_csv_text() == expected

    def test_as_csv_text_with_precision_requires_complete(self):
        ImageDataBuilder.PRECISION = BuilderRequirements.REQUIRES_COMPLETE
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14,%s,$2017.21,%s" % (Builder.SUBSTITUTE, Builder.SUBSTITUTE)
        assert image_data.as_csv_text() == expected

    def test_identifier(self):
        image_data = ImageData(test_data, image_name)
        expected = "070117-20:48:14"
        assert image_data.identifier() == expected
