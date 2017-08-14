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
        if self.f is None:
            return

        self.f.close()

    def protected_t_append(self, write_data):
        if self._temporary_query(write_data):
            return

        self._temporary_append(write_data)

    def append(self, write_data):
        if self.p_state:
            self._persisted_append(write_data)
        else:
            self._temporary_append(write_data)

    def query(self, write_data):
        # true: the item exists
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
        self._write_with_debug(write_data)

    def _temporary_append(self, write_data):
        f = open(GlobalConstants.PERSISTED_DATA_PATH, "a") #append
        self._write_with_debug(write_data, f)
        f.close()

    def _persisted_query(self, new_data):
        return self._query_with_debug(new_data)

    def _temporary_query(self, new_data):
        f = open(GlobalConstants.PERSISTED_DATA_PATH, "r") #read only
        text_found = self._query_with_debug(new_data, f)
        f.close()

        return text_found

    def _write_with_debug(self, write_data, f=None):
        if debug.LOCAL_DEBUG:
            debug.attempted_written_data(write_data.as_csv_text(), self.p_state)

        ready_data = write_data.as_csv_text() + self.NEWLINE

        getattr(self._file(f), "write")(ready_data)

        if debug.LOCAL_DEBUG:
            debug.successful_written_data(write_data.as_csv_text(), self.p_state)

    def _query_with_debug(self, new_data, f=None):
        identifier = new_data.identifier()

        if debug.LOCAL_DEBUG:
            debug.attempted_query(new_data.as_csv_text(), self.p_state)

        text = csv.reader(self._file(f), delimiter=",")
        text_found = self._find_by_identifier(text, identifier)

        if debug.LOCAL_DEBUG:
            debug.successful_query(new_data.as_csv_text(), self.p_state, text_found)

        return text_found

    def _find_by_identifier(self, text, identifier):
        if identifier is None or str(None):
            # we don't want to write None
            return True

        for row in text:
            if row[0] == identifier:
                return True

        return False

    def _file(self, f=None):
        if f is not None:
            return f
        else:
            return self.f
