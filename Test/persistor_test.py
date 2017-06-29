import unittest
import pytest
from ..Modules import persistor

class TestMethods(unittest.TestCase):
    def setup_method(self, method):
        global p
        p = persistor.Persistor()

    def teardown_method(self, method):
        p.clear_file()
        # persistor.kill()

    def test_initializa_data_file(self):
        p.initialize_data_file()

        assert(
            os.path.exists(global_constants.PERSISTED_DATA_PATH)
        )

    def test_persist(self):

        test_data = ["06/28/17-19:18:42", "Milton B 3498 Ave du parc", "4.40", "test data"]
        test_data2 = ["06/28/17-19:18:43", "Milton B 3498 Ave du parc", "4.40", "test data"]

        p.persist(test_data)
        p.persist(test_data2)

        f = open(global_constants.PERSISTED_DATA, "r")
        contents = f.read()

        expected = "06/28/17-19:18:42, Milton B 3498 Ave du parc, 4.40, test data" \
                "06/28/17-19:18:43, Milton B 3498 Ave du parc, 4.40, test data"

        assert contents == expected

    # def test_find_value(self):
    #     raise NotImplementedError
