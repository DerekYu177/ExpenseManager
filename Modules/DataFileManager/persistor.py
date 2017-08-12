import csv
import os

from ..shared import GlobalConstants
from ..shared import GlobalVariables
import data_file_helper as DataFileHelper
from ..debug import DebugPersistor as debug

debug = debug()

class Persistor:
    NEWLINE = "\n"

    def __init__(self, p_state):
        if not DataFileHelper.does_file_exist():
            DataFileHelper.initialize_data_file()

        # TODO: Use states to fix this
        # True = 'active' = leave f open for all operations
        # False = 'disabled' = require f to be opened for any operation
        self.p_state = p_state
        self._prepare_data_file()

    def close(self):
        self.f.close()

    def append(self, write_data):
        if self.p_state:
            self._persisted_append(write_data)
        else:
            self._temporary_append(write_data)

    def query(self, write_data):
        if self.p_state:
            self._persisted_query(write_data)
        else:
            self._temporary_query(write_data)

    def turn(self, new_internal_state):
        if not self.p_state and new_internal_state:
            self.f = open(GlobalConstants.PERSISTED_DATA_PATH, "r+")
        elif self.p_state and not new_internal_state:
            self.close()
        else:
            pass

    # private

    def _prepare_data_file(self):
        if self.p_state:
            self.f = open(GlobalConstants.PERSISTED_DATA_PATH, "r+")
        else:
            self.f = None

    def _persisted_append(self, write_data):
        if DataFileHelper.is_file_empty():
            self._write_with_debug(write_data)
        elif not _persisted_query(write_data):
            self._write_with_debug(write_data)
        else:
            return

    def _persisted_query(self, new_data):
        identifier = new_data.identifier()
        text = csv.reader(self.f, delimiter=",")
        return self._find_by_identifier(text, identifier)

    def _temporary_append(self, write_data):
        f = open(GlobalConstants.PERSISTED_DATA_PATH, "a") #append
        self._write_with_debug(write_data, f)
        f.close()

    def _temporary_query(self, new_data, identifier):
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

    def _write_with_debug(self, write_data, f=None):
        if debug.LOCAL_DEBUG:
            debug.attempted_written_data(write_data)

        ready_data = write_data.as_csv_text() + self.NEWLINE
        if f is not None:
            f.write(ready_data)
        else:
            self.f.write(ready_data)

        if debug.LOCAL_DEBUG:
            debug.successful_written_data(write_data)
