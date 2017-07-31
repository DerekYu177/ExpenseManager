from shared import GlobalVariables
from shared import GlobalConstants

from image_data import Core

class DebugCore:
    GLOBAL_DEBUG = False
    DEBUG_COUNTER = 0
    MAX_MESSAGE_LENGTH = 100
    VERBOSE = True
    NEWLINE = "\n"

def set_debug(debug_flag=False):
    debug_print("Set GLOBAL_DEBUG: %s" % debug_flag)
    DebugCore.GLOBAL_DEBUG = debug_flag
    DataFileHelper.LOCAL_DEBUG = debug_flag
    Persistor.LOCAL_DEBUG = debug_flag
    PhotoFileFinder.LOCAL_DEBUG = debug_flag
    ImageTextSearch.LOCAL_DEBUG = debug_flag

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

def text_truncate_access_location(location):
    # TODO
    return location

def text_tab(text, tab):
    space_number = tab * 2
    space = " "
    return space_number * space + text

def list_to_string(item_in_list, current_indentation=0):
    statement = ""
    for item in item_in_list:
        statement = statement + text_tab(item, current_indentation + 1) + DebugCore.NEWLINE
    return statement

def dict_to_string(dictionary, current_indentation=0):
    statement = ""
    for key, value in enumerable(dictionary):
        item = "%s:%s" % (key, value)
        statement = statement + (item, current_indentation + 1) + DebugCore.NEWLINE
    return statement

def print_debug_with_state(statement, ErrorState):
    # TODO
    pass

class DataFileHelper:
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

class Persistor:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def attempted_written_data(self, write_data):
        debug_print("Written: (Attempt) %s" % (write_data))

    def successful_written_data(self, write_data):
        debug_print("Written: (Success) %s" % (write_data))

class PhotoFileFinder:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def print_all_photo_files_in_location(self, observed_photos):
        statement = ("Receipt location: %s" % GlobalVariables.RECEIPT_LOCATION) + DebugCore.NEWLINE
        statement = statement + list_to_string(observed_photos, 0) + DebugCore.NEWLINE
        debug_print(statement)

class ImageTextSearch:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def show_set_attributes(self, attr, attr_value):
        debug_print("Set %s: %s" % (attr, attr_value))

    def text_and_relevant_text(self, original_text, relevant_text):
        statement = "Original Text:" + dict_to_string(original_text) + DebugCore.NEWLINE
        statement = statement + "Relevant text:" + dict_to_string(relevant_text) + DebugCore.NEWLINE
        debug_print(statement)

    def append_original_text(self, text):
        return {
            "original text": text,
        }

    def all_set_attributes(self, obj):
        statement = "Retriving attributes:"

        for attr in Core.ANALYSIS_ATTRIBUTES:
            message = "Get %s: %s" % (attr, obj.__dict__[attr])
            statement = statement + text_tab(message, 1)

        debug_print(statement)

class ErrorState:

    def __init__(self, state):
        # TODO
        pass
