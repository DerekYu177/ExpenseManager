import unittest
import pytest
from ExpenseManager.Modules import file_accessor

class TestMethods(unittest.TestCase):
    # def test_all_images_in_location(self):
    #     raise NotImplementedError

    def test_list_to_string(self):
        test_list = ["a", "b", "c", "d"]
        actual = file_accessor.list_to_string(test_list)
        expected = "a \n b \n c \n d"

        assert actual == expected

    # def test_prompt_user_for_location(self):
    #     raise NotImplementedError
