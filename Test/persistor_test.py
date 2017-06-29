import unittest, pytest, os
from ..Modules import persistor
from ..Modules.shared import global_constants as global_constants
from ..Modules.shared import global_variables as global_variables


class TestMethods(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        global p
        p = persistor.Persistor()

    @classmethod
    def teardown_class(cls):
        p.clear_file()

    def test_initializa_data_file(self):
        global_variables.DEBUG = True
        p.initialize_data_file()

        assert os.path.isfile(global_constants.PERSISTED_DATA_PATH)

    def test_persist(self):

        test_data = ["06/28/17-19:18:42", "Milton B 3498 Ave du parc", "4.40", "test data"]
        test_data2 = ["06/28/17-19:18:43", "Milton B 3498 Ave du parc", "4.40", "test data"]

        p.persist(test_data)
        p.persist(test_data2)

        f = open(global_constants.PERSISTED_DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "06/28/17-19:18:42,Milton B 3498 Ave du parc,4.40,test data\n06/28/17-19:18:43,Milton B 3498 Ave du parc,4.40,test data\n"

        assert contents == expected

    def clear_file(self):
        test_data = ["06/28/17-19:18:42", "Milton B 3498 Ave du parc", "4.40", "test data"]

        p.persist(test_data)
        p.clear_file()

        assert p.is_file_empty()

    # def test_find_value(self):
    #     raise NotImplementedError
