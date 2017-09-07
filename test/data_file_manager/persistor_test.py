import unittest, pytest
import os
from ...modules.data_file_manager import persistor
from .. import test_helper

from ...modules import shared
from ...modules import image_data
from ...modules.data_file_manager import data_file_helper

class TestMethods(unittest.TestCase, test_helper.TestHelper):
    def setup(self):
        global id1, id2
        data_file_helper.initialize_data_file()
        image_name = "dank_memes.jpg"

        id1 = image_data.ImageData({
            "date": "07/01/17",
            "time": "20:48:14",
            "address": "None",
            "total_amount": "$2017.21",
            "description": "test data"
        }, image_name)

        id2 = image_data.ImageData({
            "date": "07/01/17",
            "time": "20:48:50",
            "address": "None",
            "total_amount": "$20.17",
            "description": "test data"
        }, image_name)

    def teardown_method(self, method):
        data_file_helper.clear_file()
        data_file_helper.del_file()

    def test_persist_data_with_persisted_state_enabled(self):
        self.setup()
        p = persistor.Persistor(True)
        p.append(id1)
        p.append(id2)
        p.close()

        f = open(shared.GlobalVariables.DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "070117,2048(14),None,$2017.21,test data\n070117,2048(50),None,$20.17,test data\n"

        assert contents == expected

    def test_query_with_persisted_state_enabled(self):
        self.setup()
        p = persistor.Persistor(True)
        p.append(id1)
        p.append(id2)

        result = p.query(id2)
        assert result == image_data.ExistanceState.EXISTS
        p.close()

    def test_persist_data_with_persisted_state_disabled(self):
        self.setup()
        p = persistor.Persistor(False)
        p.append(id1)
        p.append(id2)
        p.close()

        f = open(shared.GlobalVariables.DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "070117,2048(14),None,$2017.21,test data\n070117,2048(50),None,$20.17,test data\n"

        assert contents == expected

    def test_query_with_persisted_state_disabled(self):
        self.setup()
        p = persistor.Persistor(False)
        p.append(id1)
        p.append(id2)

        result = p.query(id2)
        assert result is image_data.ExistanceState.EXISTS
        p.close()

    def test_protected_append_with_all_none_does_not_write_to_file(self):
        p = persistor.Persistor(False)
        none_image_data = image_data.ImageData({
            "date": None,
            "time": None,
            "address": None,
            "total_amount": None,
            "description": None
        }, "ALL NONE")
        result = p.protected_append(none_image_data)
        assert data_file_helper.is_file_empty()
        assert result is image_data.ExistanceState.NONE
