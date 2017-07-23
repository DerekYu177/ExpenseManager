import unittest
import pytest
from ...Modules.PhotoAnalyzer import image_processor
from ...Modules.image_data import ImageData

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
        image_processor.LOCAL_DEBUG = True

    def test_find_date(self):
        assert "07/01/17" == its._find_date()

    def test_find_time(self):
        assert "20:48:14" == its._find_time()

    def test_find_address(self):
        assert None == its._find_address()

    def test_find_total_amount(self):
        assert "$2017.21" == its._find_total_amount()

    def test_description(self):
        assert None == its._find_description()

    def test_analyze(self):
        attrs = {
            "date": "07/01/17",
            "time": "20:48:14",
            "address": None,
            "total_amount": "$2017.21",
            "description": None,
        }

        assert its.is_photo

        image_data = its.analyze()

        assert isinstance(image_data, ImageData)

        print image_data

        for attr, attr_val in attrs.iteritems():
            assert(attr_val == image_data.__dict__[attr])

    def test_is_photo_receipt(self):
        its = image_processor.ImageTextSearch("text")

        assert its.is_photo == False
