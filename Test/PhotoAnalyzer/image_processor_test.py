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

    def test_find_datetime(self):
        expected = {
            "date": "07/01/17",
            "time": "20:48:14"
        }

        assert expected == its.find_datetime()

    def test_find_address(self):
        expected = {
            "address": "None"
        }

        assert expected == its.find_address()

    def test_find_total_amount(self):
        expected = {
            "total_amount": "$2017.21"
        }

        assert expected == its.find_total_amount()

    def test_description(self):
        expected = {
            "description": "None"
        }

        assert expected == its.description()

    def test_analyze(self):
        attrs = {
            "date": "07/01/17",
            "time": "20:48:14",
            "address": "None",
            "total_amount": "$2017.21",
            "description": "None"
        }

        image_data = its.analyze()

        assert isinstance(image_data, ImageData)

        print image_data

        for attr, attr_val in attrs.iteritems():
            assert(attr_val == image_data.__dict__[attr])
