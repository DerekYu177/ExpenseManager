import unittest, pytest, os
from ..Modules.persistor import Persistor
from ..Modules.shared import GlobalConstants
from ..Modules.shared import GlobalVariables
from ..Modules.image_data import ImageData
from ..Modules.data_file_helper import DataFileHelper

class TestMethods(unittest.TestCase):
    def setup_method(self, method):
        global id1, id2, p, dfh

        dfh = DataFileHelper()
        dfh.initialize_data_file()
        
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

    # we need to teardown after every method
    def teardown_method(self, method):
        dfh.clear_file()

    def test_persist(self):

        GlobalVariables.DEBUG = True

        p.persist(id1)
        p.persist(id2)

        f = open(GlobalConstants.PERSISTED_DATA_PATH, "r")
        contents = f.read()
        f.close()

        expected = "070117-20:48:14,None,$2017.21,test data\n070117-20:48:50,None,$20.17,test data\n"

        assert contents == expected

    def test_does_data_exist(self):
        p.persist(id1)
        p.persist(id2)

        assert p.does_data_exist(id2) == True
