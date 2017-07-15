import unittest, pytest, os
from ..Modules import persistor
from ..Modules.shared import global_constants as global_constants
from ..Modules.shared import global_variables as global_variables


class TestMethods(unittest.TestCase):
    def setup_method(self, method):
        global p, test_data, test_data2
        p = persistor.Persistor()

        test_data = ["06/28/17-19:18:42", "Milton B 3498 Ave du parc", "4.40", "test data"]
        test_data2 = ["06/28/17-19:18:43", "Milton B 3498 Ave du parc", "4.40", "test data"]

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

        expected = "06/28/17-19:18:42,Milton B 3498 Ave du parc,4.40,test data\n06/28/17-19:18:43,Milton B 3498 Ave du parc,4.40,test data\n"

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
