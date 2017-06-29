import unittest
import pytest
from ..Modules import file_accessor as file_accessor

class TestMethods(unittest.TestCase):
    def test_all_images_in_location(self):
        raise NotImplementedError

    def test_print_list_to_string(self):
        test_list = ["a", "b", "c", "d"]
        actual = file_accessor.print_list_to_string(test_list)
        expected = "a\nb\nc\nd\n"

        assert actual == expected

    def test_prompt_user_for_location(self):
        raise NotImplementedError
