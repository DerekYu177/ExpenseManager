import unittest
import pytest
from .modules.pa import finder
from .modules.image_data import ImageData

class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global f

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

        f = finder.Finder(text)

    def test_find_date(self):
        assert "07/01/2017" == f.find_date()

    def test_find_time(self):
        assert "20:48:14" == f.find_time()

    def test_find_address(self):
        assert None == f.find_address()

    def test_find_total_amount(self):
        assert "$2017.21" == f.find_total_amount()

    def test_description(self):
        assert None == f.find_description()
