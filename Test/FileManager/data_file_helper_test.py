import unittest, pytest, os
from ..Modules.data_file_helper import DataFileHelper
from ..Modules.shared import GlobalConstants
from ..Modules.shared import GlobalVariables

class TestMethods(unittest.TestCase):
    def test_create_and_destroy_file(self):
        dfh = DataFileHelper()
        dfh.initialize_data_file()

        assert dfh.does_file_exist() == True

        dfh.clear_file()

        assert dfh.is_file_empty() == True
