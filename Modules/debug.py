from enum import Enum

from shared import GlobalVariables
from shared import GlobalConstants
from shared import ImageDataCore

class DebugCore:
    GLOBAL_DEBUG = False
    DEBUG_COUNTER = 0
    MAX_MESSAGE_LENGTH = 100
    VERBOSE = True
    NEWLINE = "\n"

def set_debug(debug_flag=False):
    debug_print("Set GLOBAL_DEBUG: %s" % debug_flag)
    DebugCore.GLOBAL_DEBUG = debug_flag
    DebugDataFileHelper.LOCAL_DEBUG = debug_flag
    DebugPersistor.LOCAL_DEBUG = debug_flag
    DebugPhotoFileFinder.LOCAL_DEBUG = debug_flag
    DebugImageProcessor.LOCAL_DEBUG = debug_flag
    DebugImageData.LOCAL_DEBUG = debug_flag

def show_sys_path():
    import sys
    for path in sys.path:
        print path

def debug_print(text):
    text = text_truncate(text)
    print "%s: %s" % (DebugCore.DEBUG_COUNTER, text)
    # add condition where there is a new line involved
    DebugCore.DEBUG_COUNTER = DebugCore.DEBUG_COUNTER + 1

def text_truncate(text):
    if DebugCore.VERBOSE or len(text) < DebugCore.MAX_MESSAGE_LENGTH:
        return text

    text = text[:DebugCore.MAX_MESSAGE_LENGTH-3]
    text = text + "..."
    return text

def safe_none(attr):
    if attr is None:
        return str(attr)

def text_truncate_access_location(location):
    return location # TODO

def text_tab(text, tab):
    space_number = tab * 3
    space = " "
    return space_number * space + text

def indent_text(text, current_indentation=0):
    statement = DebugCore.NEWLINE
    for line in text.split(DebugCore.NEWLINE):
        statement = statement + text_tab(line, current_indentation + 1) + DebugCore.NEWLINE
    return statement

def list_to_string(item_in_list, current_indentation=0):
    statement = DebugCore.NEWLINE
    for item in item_in_list:
        statement = statement + text_tab(item, current_indentation + 1) + DebugCore.NEWLINE
    return statement

def dict_to_string(dictionary, current_indentation=0):
    statement = DebugCore.NEWLINE
    for key, value in dictionary.items():
        item = "%s:%s" % (key, value)
        statement = statement + text_tab(item, current_indentation + 1) + DebugCore.NEWLINE
    return statement

def print_debug_with_state(statement, ErrorState):
    # TODO: When states are enabled
    pass

class DebugService: #TODO
    def __init__(self):
        pass

    def show_image_data(self, image_data):
        pass

class DebugDataFileHelper:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def file_and_directory(self, file_path, directory_exists, file_exists):
        statement = "File path: %s" % (file_path) + DebugCore.NEWLINE
        statement = statement + "Directory exist?: %s" % (directory_exists) + DebugCore.NEWLINE
        statement = statement + "File exist?: %s" % (file_exists) + DebugCore.NEWLINE
        debug_print(statement)

    def successful_file_and_directory_created(self, file_path):
        debug_print("File/Dir Created: (success) at %s" % (file_path))

class DebugPersistor:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def attempted_query(self, write_data, p_state):
        statement = "Query: (Attempt) (%s) %s" % (self._p_state(p_state), write_data)
        debug_print(statement)

    def successful_query(self, write_data, p_state, result):
        statement = "Query: (Success) (%s) (%s) %s" % (self._p_state(p_state), self._result(result), write_data)
        debug_print(statement)

    def attempted_written_data(self, write_data, p_state):
        statement = "Write: (Attempt) (%s) %s" % (self._p_state(p_state), write_data)
        debug_print(statement)

    def successful_written_data(self, write_data, p_state):
        statement = "Write: (Success) (%s) %s" % (self._p_state(p_state), write_data)
        debug_print(statement)

    def _p_state(self, p_state):
        if p_state:
            return "Persisted"
        else:
            return "Temporary"

    def _result(self, result):
        return result.name

class DebugPhotoFileFinder:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def print_all_photo_files_in_location(self, observed_photos):
        statement = ("Receipt location: %s" % GlobalVariables.RECEIPT_LOCATION) + DebugCore.NEWLINE
        statement = statement + list_to_string(observed_photos, 0) + DebugCore.NEWLINE
        debug_print(statement)

class DebugImageProcessor:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def show_image_name(self, image_location):
        statement = "The current photo is:" + image_location
        debug_print(statement)

    def show_set_attributes(self, attr, attr_value):
        debug_print("Set %s: %s" % (attr, attr_value))

    def text_and_relevant_text(self, original_text, relevant_text):
        statement_1 = "Original Text:" + DebugCore.NEWLINE
        statement_1 = statement_1 + indent_text(original_text)
        debug_print(statement_1)

        statement_2 = "Relevant text:" + dict_to_string(relevant_text) + DebugCore.NEWLINE
        debug_print(statement_2)

    def append_original_text(self, text):
        return {
            "original text": text,
        }

    def all_set_attributes(self, obj):
        statement = "Retriving attributes:"

        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            message = "Get %s: %s" % (attr, obj.__dict__[attr])
            statement = statement + text_tab(message, 1)

        debug_print(statement)

    def show_full_data(self, filled_data):
        statement = dict_to_string(filled_data)
        debug_print(statement)

class DebugImageData:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def show_csv_text(self, joined_text):
        statement = "Data:" + joined_text
        debug_print(statement)

class DebugState(Enum):
    NOMINAL = 0
    STATUS = 1
    VERBOSE = 2
