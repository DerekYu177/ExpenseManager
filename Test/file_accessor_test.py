import unittest
import pytest
from ..Modules import file_accessor as file_accessor
from ..Modules import shared as shared

class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global pf
        pf = file_accessor.PhotoFinder()

    def test_print_list_to_string(self):
        test_list = ["a", "b", "c", "d"]
        actual = pf.print_list_to_string(test_list)
        expected = "a\nb\nc\nd\n"

        assert actual == expected

    def test_print_list_to_string_when_list_not_list(self):
        test_list = "/Shared/DerekYu177"
        assert pf.print_list_to_string(test_list) == test_list

    def test_find_photos_when_glb_var_not_instantiated_raises_error(self):
        shared.GlobalVariables.RECEIPT_LOCATION = ""
        with pytest.raises(EnvironmentError) as error:
            pf.find_photos()
        error.match(r'Receipt location not initialized')

    def test_find_photos(self):
        shared.GlobalVariables.RECEIPT_LOCATION = shared.GlobalVariables.IMAGE_LOCATION

        assert len(pf.find_photos()) == 5

    def test_is_photo(self):
        test_list_of_photos = {
            "high_def_receipt.jpg": True,
            "text.png": True,
            "text_advanced.gif": False,
            "text_colors.jpg": True,
        }

        for name, result in test_list_of_photos.iteritems():
            assert pf.is_photo(name) == result
