import csv
import os
from enum import Enum

import data_file_helper
from ..shared import GlobalVariables
from ..debug import DebugPersistor as debug

debug = debug()

class Persistor:
    NEWLINE = "\n"

    def __init__(self, p_state):
        if not data_file_helper.does_file_exist():
            data_file_helper.initialize_data_file()

        # True = leave f open for all operations
        self.p_state = p_state
        self._prepare_data_file()
        self.last_action = LastAction.INIT

    def close(self):
        if self.p_state:
            self.f.close()
        else:
            return

    def protected_append(self, write_data):
        self.p_state = False
        state = self.query(write_data)
        if (state is Identification.EXISTS) or (state is Identification.IS_NONE):
            return

        self.append(write_data)

    def append(self, write_data):
        if self.p_state:
            self._persisted_append(write_data)
        else:
            self._temporary_append(write_data)

    def query(self, write_data):
        # true: the item exists
        if self.p_state:
            return self._persisted_query(write_data)
        else:
            return self._temporary_query(write_data)

    def turn(self, new_internal_state):
        if not self.p_state and new_internal_state:
            self.f = open(GlobalVariables.DATA_PATH, "r+")
        elif self.p_state and not new_internal_state:
            self.close()
        else:
            pass

    def _prepare_data_file(self):
        if self.p_state:
            self.f = open(GlobalVariables.DATA_PATH, "r+")
        else:
            self.f = None

    def _persisted_append(self, write_data):
        self._append_with_debug(write_data)

    def _temporary_append(self, write_data):
        f = open(GlobalVariables.DATA_PATH, "a") #append
        self._append_with_debug(write_data, f)
        f.close()

    def _persisted_query(self, new_data):
        return self._query_with_debug(new_data)

    def _temporary_query(self, new_data):
        f = open(GlobalVariables.DATA_PATH, "r") #read only
        text_found = self._query_with_debug(new_data, f)
        f.close()

        return text_found

    def _append_with_debug(self, write_data, f=None):
        debug.attempted_written_data(str(write_data), self.p_state)
        ready_data = str(write_data) + self.NEWLINE
        getattr(self._file(f), "write")(ready_data)
        debug.successful_written_data(str(write_data), self.p_state)
        self.last_action = LastAction.APPEND

    def _query_with_debug(self, new_data, f=None):
        identifier = new_data.identifier()
        self._refresh_file()
        debug.attempted_query(str(new_data), self.p_state)
        openable_file = self._file(f)
        text = csv.reader(openable_file, delimiter=",")
        text_found = self._find_by_identifier(text, identifier)
        debug.successful_query(str(new_data), self.p_state, text_found)
        self.last_action = LastAction.QUERY

        return text_found

    def _find_by_identifier(self, text, identifier):
        if (identifier is None) or (identifier is str(None)):
            # we don't want to write None
            return Identification.IS_NONE

        for row in text:
            if row[0] == identifier:
                return Identification.EXISTS

        return Identification.NEW_ENTRY

    def _file(self, f=None):
        if self.f:
            return self.f
        else:
            return f

    def _refresh_file(self):
        if self.p_state and (self.last_action is LastAction.APPEND):
            self._refresh()
        return

    def _refresh(self):
        self.f.close()
        # flush cache
        self.f = open(GlobalVariables.DATA_PATH, "r+")

class Identification(Enum):
    NEW_ENTRY = 0
    EXISTS = 1
    IS_NONE = 2

class LastAction(Enum):
    INIT = 0
    APPEND = 1
    QUERY = 2
    SORT = 3
