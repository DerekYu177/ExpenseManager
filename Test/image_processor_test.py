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

            amount: $ 2017.21

            $  3000.1

            $ 291.20
            """

        s = image_processor.ImageText(text)


    def test_find_datetime(self):
        expected = {
            "date": "07/01/17",
            "time": "20:48:14"
        }

        assert expected == s.find_datetime()

    def test_find_address(self):
        expected = {
            "address": "None"
        }

        assert expected == s.find_address()

    def test_find_total_amount(self):
        expected = {
            "total_amount": "$2017.21"
        }

        assert expected == s.find_total_amount()

    def test_description(self):
        expected = {
            "description": "None"
        }

        assert expected == s.description()

    def test_relevant_text(self):
        expected = {
            "date": "07/01/17",
            "time": "20:48:14",
            "address": "None",
            "total_amount": "$2017.21",
            "description": "None"
        }

        assert expected == s.relevant_text()
