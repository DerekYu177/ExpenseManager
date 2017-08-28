import unittest
import pytest

from ... Modules.dfm import photo_file_finder
from ...Modules.shared import GlobalVariables

class TestMethods(unittest.TestCase):
    def test_find_photos_when_glb_var_not_instantiated_raises_error(self):
        GlobalVariables.RECEIPT_LOCATION = ""

        with pytest.raises(EnvironmentError) as error:
            photo_file_finder.find_photos()
        error.match(r'Receipt location not initialized')

    def test_find_photos(self):
        GlobalVariables.RECEIPT_LOCATION = GlobalVariables.IMAGE_LOCATION

        assert len(photo_file_finder.find_photos()) == 5

    def test_is_photo(self):
        test_list_of_photos = {
            "high_def_receipt.jpg": True,
            "text.png": True,
            "text_advanced.gif": False,
            "text_colors.jpg": True,
        }

        for name, result in test_list_of_photos.iteritems():
            assert photo_file_finder.is_photo(name) == result
