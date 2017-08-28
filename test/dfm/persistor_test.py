import unittest, pytest
import os
from ...m.dfm import persistor

from ...m import shared
from ...m.image_data import ImageData
from ...m.dfm import data_file_helper

class TestMethods(unittest.TestCase):
    def setup_method(self, method):
        global id1, id2

        data_file_helper.initialize_data_file()

        id1 = ImageData({
            "date": "07/01/17",
            "time": "20:48:14",
            "address": "None",
            "total_amount": "$2017.21",
            "description": "test data"
        })

        id2 = ImageData({
            "date": "07/01/17",
            "time": "20:48:50",
            "address": "None",
            "total_amount": "$20.17",
            "description": "test data"
        })

    def teardown_method(self, method):
        data_file_helper.clear_file()
        data_file_helper.del_file()

    def test_persist_data_with_persisted_state_enabled(self):
        p = persistor.Persistor(True)
        p.append(id1)
        p.append(id2)
        p.close()

        f = open(shared.GlobalConstants.PERSISTED_DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "070117-20:48:14,None,$2017.21,test data\n070117-20:48:50,None,$20.17,test data\n"

        assert contents == expected

    def test_query_with_persisted_state_enabled(self):
        p = persistor.Persistor(True)
        p.append(id1)
        p.append(id2)

        result = p.query(id2)
        assert result == persistor.Identification.EXISTS
        p.close()

    def test_persist_data_with_persisted_state_disabled(self):
        p = persistor.Persistor(False)
        p.append(id1)
        p.append(id2)
        p.close()

        f = open(shared.GlobalConstants.PERSISTED_DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "070117-20:48:14,None,$2017.21,test data\n070117-20:48:50,None,$20.17,test data\n"

        assert contents == expected

    def test_query_with_persisted_state_disabled(self):
        p = persistor.Persistor(False)
        p.append(id1)
        p.append(id2)

        result = p.query(id2)
        assert result == persistor.Identification.EXISTS
        p.close()
