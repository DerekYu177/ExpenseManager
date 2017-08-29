import unittest
import pytest
from ...modules.photo_analyzer import image_processor
from ...modules.image_data import ImageData

class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global its

        text = """
            caFE PARVIS
            433 RUE nnvon
            MONTREAL. nc Han 1N9
            Merchant ID: aaeaeeausasssss

            Term ID: ass79245
            25350990016

            Purchase

            Entrv Hethod: Chin

            , 07/01/17 20:48:14

            $0.01
            $0.02
            #1.24
            $1293.17
            $4.04
            $192.19362

            amount: $ 2017.21

            $  3000.1

            $ 291.20
            """

        its = image_processor.ImageTextSearch(text)

    def test_analyze(self):
        csv_text = "07012017-20:48:14,None,$2017.21,None"
        image_data = its.analyze()
        assert isinstance(image_data, ImageData)
        assert csv_text, image_data.as_csv_text()
