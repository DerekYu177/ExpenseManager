import unittest, pytest, os
from ..Modules import persistor
from ..Modules.shared import global_constants
from ..Modules.shared import global_variables


class TestMethods(unittest.TestCase):
    def setup_method(self, method):
        global i, p, test_data, test_data2

        test_data = {
            "date": "07/01/17",
            "time": "20:48:14",
            "address": "None",
            "total_amount": "$2017.21",
            "description": "test data"
        }

        test_data2 = {
            "date": "07/01/17",
            "time": "20:48:50",
            "address": "None",
            "total_amount": "$20.17",
            "description": "test data"
        }

        p = persistor.Persistor()

    # we need to teardown after every method
    def teardown_method(self, method):
        p.clear_file()

    def test_initializa_data_file(self):
        p.initialize_data_file()

        assert os.path.isfile(global_constants.PERSISTED_DATA_PATH)

    def test_persist(self):

        global_variables.DEBUG = True

        p.persist(test_data)
        p.persist(test_data2)

        f = open(global_constants.PERSISTED_DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "07/01/17-20:48:14,None,$2017.21,test data\n07/01/17-20:48:50,None,$20.17,test data\n"

        assert contents == expected

    def test_does_data_exist(self):
        p.persist(test_data)
        p.persist(test_data2)

        assert p.does_data_exist(test_data2) == True

    def test_clear_file(self):
        p.persist(test_data)
        p.clear_file()

        assert p.is_file_empty()

    # def test_find_value(self):
    #     raise NotImplementedError
