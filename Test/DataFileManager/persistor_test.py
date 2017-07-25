import unittest, pytest
import os
from ...Modules.DataFileManager.persistor import Persistor

from ...Modules import shared
from ...Modules.image_data import ImageData
from ...Modules.DataFileManager import data_file_helper as DataFileHelper

class TestMethods(unittest.TestCase):
    def setup_method(self, method):
        global id1, id2, p

        DataFileHelper.initialize_data_file()

        p = Persistor()

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
        DataFileHelper.clear_file()
        DataFileHelper.del_file()

    def test_persist_data(self):
        p.append(id1)
        p.append(id2)
        p.close()

        f = open(shared.GlobalConstants.PERSISTED_DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "070117-20:48:14,None,$2017.21,test data\n070117-20:48:50,None,$20.17,test data\n"

        assert contents == expected

    def test_does_data_exist(self):
        p.append(id1)
        p.append(id2)
        p.close()

        assert p.does_data_exist(id2)
