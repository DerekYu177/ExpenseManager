import unittest
import pytest
import os

from .. import test_helper
from ...modules.data_file_manager import data_file_helper

class TestMethods(unittest.TestCase, test_helper.TestHelper):
    def test_create_and_destroy_file(self):
        data_file_helper.initialize_data_file()
        assert data_file_helper.does_file_exist() == True
        data_file_helper.clear_file()
        assert data_file_helper.is_file_empty() == True
