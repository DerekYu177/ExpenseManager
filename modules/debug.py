from enum import Enum
from functools import wraps

from shared import GlobalVariables
from shared import GlobalConstants
from shared import State
from CLI import PrintCore
from CLI import Printer

SOURCE = "DEBUG"

def can_call(func):
    @wraps(func)
    def respond_depending_on_state(*args):
        klass = args[0]
        global_state = GlobalVariables.STATE
        if (global_state is State.NOMINAL):
            return
        elif (global_state is State.TEST):
            return
        elif (global_state is State.DEBUG_BASIC) and not _is_verbose(func, klass):
            return func(*args)
        elif (global_state is State.DEBUG_VERBOSE) and _is_verbose(func, klass):
            return func(*args)
        else:
            return

    return respond_depending_on_state

def _is_verbose(function, klass):
    if (function.func_name in klass.VERBOSE_METHODS):
        return True
    else:
        return False

class DebugService(Printer, PrintCore): #TODO
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    def show_image_data(self, image_data):
        pass

class DebugDataFileHelper(Printer, PrintCore):
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    @can_call
    def file_and_directory(self, file_path, directory_exists, file_exists):
        statement = "File path: %s" % (file_path) + self.NEWLINE
        statement = statement + "Directory exist?: %s" % (directory_exists) + self.NEWLINE
        statement = statement + "File exist?: %s" % (file_exists) + self.NEWLINE
        self.show(SOURCE, statement)

    @can_call
    def successful_file_and_directory_created(self, file_path):
        self.show(SOURCE, "File/Dir Created: (success) at %s" % (file_path))

class DebugPersistor(Printer, PrintCore):
    VERBOSE_METHODS = [
        "attempted_query",
        "attempted_written_data"
    ]

    def __init__(self):
        pass

    @can_call
    def attempted_query(self, write_data, p_state):
        statement = "Query: (Attempt) (%s) %s" % (self._p_state(p_state), write_data)
        self.show(SOURCE, statement)

    @can_call
    def successful_query(self, write_data, p_state, result):
        statement = "Query: (Success) (%s) (%s) %s" % (self._p_state(p_state), self._result(result), write_data)
        self.show(SOURCE, statement)

    @can_call
    def attempted_written_data(self, write_data, p_state):
        statement = "Write: (Attempt) (%s) %s" % (self._p_state(p_state), write_data)
        self.show(SOURCE, statement)

    @can_call
    def successful_written_data(self, write_data, p_state):
        statement = "Write: (Success) (%s) %s" % (self._p_state(p_state), write_data)
        self.show(SOURCE, statement)

    def _p_state(self, p_state):
        if p_state:
            return "Persisted"
        else:
            return "Temporary"

    def _result(self, result):
        return result.name

class DebugPhotoFileFinder(Printer, PrintCore):
    VERBOSE_METHODS = [
        "all_photos_in_location"
    ]

    def __init__(self):
        pass

    @can_call
    def location(self):
        statement = ("Receipt location: %s" % GlobalVariables.RECEIPT_LOCATION)
        self.show(SOURCE, statement)

    @can_call
    def all_photos_in_location(self, observed_photos):
        statement = self.list_to_string(observed_photos, 0)
        self.show(SOURCE, statement)

class DebugImageProcessor(Printer, PrintCore):
    VERBOSE_METHODS = [
        "text_and_relevant_text"
    ]

    def __init__(self):
        pass

    def append_original_text(self, text):
        return {
            "original text": text,
        }

    @can_call
    def show_image_name(self, image_location):
        statement = "Current photo:" + image_location
        self.show(SOURCE, statement)

    @can_call
    def show_set_attributes(self, attr, attr_value):
        self.show(SOURCE, "Set %s: %s" % (attr, attr_value))

    @can_call
    def text_and_relevant_text(self, original_text, relevant_text):
        statement = "Original Text:" + self.NEWLINE
        statement = statement + self.indent_text(original_text)
        self.show(SOURCE, statement)

        statement = "Relevant text:" + self.dict_to_string(relevant_text) + self.NEWLINE
        self.show(SOURCE, statement)

    @can_call
    def show_full_data(self, filled_data):
        statement = self.dict_to_string(filled_data)
        self.show(SOURCE, statement)

class DebugImageData(Printer, PrintCore):
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    @can_call
    def show_csv_text(self, joined_text):
        statement = "Data:" + joined_text
        self.show(SOURCE, statement)
