import unittest
import pytest
from ..Modules import image_processor as image_processor

class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global s

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
            """

        s = image_processor.SearchableText(text)


    def test_find_datetime(self):
        expected = {
            "date": "07/01/17",
            "time": "20:48:14"
        }

        assert expected == s.find_datetime()

    def test_find_total_amount(self):
        expected = {
            "total_amount": "$1293.17"
        }

        assert expected == s.find_total_amount()
