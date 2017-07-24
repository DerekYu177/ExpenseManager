import unittest, pytest
import os

from ...Modules.DataFileManager import data_file_helper

class TestMethods(unittest.TestCase):
    def test_create_and_destroy_file(self):
        DataFileHelper.initialize_data_file()

        assert DataFileHelper.does_file_exist() == True

        DataFileHelper.clear_file()

        assert DataFileHelper.is_file_empty() == True
