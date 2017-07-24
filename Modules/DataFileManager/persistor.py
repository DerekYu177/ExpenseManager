import csv
import os

from ..shared import GlobalConstants
import data_file_helper as DataFileHelper

LOCAL_DEBUG = False

class Persistor:

    def __init__(self):
        if not DataFileHelper.does_file_exist():
            DataFileHelper.initialize_data_file()

        self.f = open(GlobalConstants.PERSISTED_DATA_PATH, "r+") # read/write

    def close(self):
        self.f.close()

    def append(self, write_data):
        if self.f.closed: return self._tmp_append(write_data)

        if LOCAL_DEBUG: self.__debug_attempted_written_data(write_data)
        self.f.write(self._with_newline(write_data.as_csv_text()))
        if LOCAL_DEBUG: self.__debug_successful_written_data(write_data)

    def does_data_exist(self, new_data):
        identifier = new_data.identifier()

        if self.f.closed: return self._tmp_does_data_exist(new_data, identifier)

        text = csv.reader(self.f, delimiter=",")
        return self._find_by_identifier(text, identifier)

    def _tmp_append(self, write_data):
        f = open(GlobalConstants.PERSISTED_DATA_PATH, "a") #append

        if LOCAL_DEBUG: self.__debug_attempted_written_data(write_data)
        f.write(self._with_newline(write_data.as_csv_text()))
        if LOCAL_DEBUG: self.__debug_successful_written_data(write_data)
        f.close()

    def _tmp_does_data_exist(self, new_data, identifier):
        f = open(GlobalConstants.PERSISTED_DATA_PATH, "r") #read only
        text = csv.reader(f, delimiter=",")
        text_found = self._find_by_identifier(text, identifier)
        f.close()

        return text_found

    def _find_by_identifier(self, text, identifier):
        for row in text:
            if row[0] == identifier:
                return True

        return False

    def _with_newline(self, write_data):
        return write_data + "\n"

    def __debug_attempted_written_data(self, write_data):
        print "Data attempted to be written to file: %s" % (write_data)

    def __debug_successful_written_data(self, write_data):
        print "Data successfully written to file   : %s" % (write_data)
