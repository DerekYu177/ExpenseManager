from enum import Enum
from functools import wraps

from shared import GlobalVariables
from shared import GlobalConstants
from shared import ImageDataCore

def can_call(func):
    @wraps(func)
    def respond_depending_on_state(*args):
        klass = args[0]
        state = klass.CALL_STATUS
        if (state is DebugState.BASIC) and not _is_verbose(func, klass):
            return func(*args)
        elif (state is DebugState.VERBOSE):
            return func(*args)
        return

    return respond_depending_on_state

def _is_verbose(function, klass):
    if (function.func_name in klass.VERBOSE_METHODS):
        return True
    else:
        return False

class DebugState(Enum):
    OFF = 0
    BASIC = 1
    VERBOSE = 2

class DebugCore:
    GLOBAL_DEBUG = DebugState.OFF
    DEBUG_COUNTER = 0
    MAX_MESSAGE_LENGTH = 100
    VERBOSE_METHODS = True
    NEWLINE = "\n"

class BaseDebug:
    def set_debug(self, debug_flag=DebugState.OFF):
        self.debug_print("Set GLOBAL_DEBUG: %s" % debug_flag.name)
        DebugCore.GLOBAL_DEBUG = debug_flag
        DebugDataFileHelper.CALL_STATUS = debug_flag
        DebugPersistor.CALL_STATUS = debug_flag
        DebugPhotoFileFinder.CALL_STATUS = debug_flag
        DebugImageProcessor.CALL_STATUS = debug_flag
        DebugImageData.CALL_STATUS = debug_flag

    def show_sys_path(self):
        import sys
        for path in sys.path:
            print path

    def debug_print(self, text):
        text = self.text_truncate(text)
        print "%s: %s" % (DebugCore.DEBUG_COUNTER, text)
        # add condition where there is a new line involved
        DebugCore.DEBUG_COUNTER = DebugCore.DEBUG_COUNTER + 1

    def text_truncate(self, text):
        if DebugCore.VERBOSE_METHODS or len(text) < DebugCore.MAX_MESSAGE_LENGTH:
            return text

        text = text[:DebugCore.MAX_MESSAGE_LENGTH-3]
        text = text + "..."
        return text

    def text_truncate_access_location(self, location):
        return location # TODO

    def text_tab(self, text, tab):
        space_number = tab * 3
        space = " "
        return space_number * space + text

    def indent_text(self, text, current_indentation=0):
        statement = DebugCore.NEWLINE
        for line in text.split(DebugCore.NEWLINE):
            statement = statement + self.text_tab(line, current_indentation + 1) + DebugCore.NEWLINE
        return statement

    def list_to_string(self, item_in_list, current_indentation=0):
        statement = DebugCore.NEWLINE
        for item in item_in_list:
            statement = statement + self.text_tab(item, current_indentation + 1) + DebugCore.NEWLINE
        return statement

    def dict_to_string(self, dictionary, current_indentation=0):
        statement = DebugCore.NEWLINE
        for key, value in dictionary.items():
            item = "%s:%s" % (key, value)
            statement = statement + self.text_tab(item, current_indentation + 1) + DebugCore.NEWLINE
        return statement

class DebugService(BaseDebug): #TODO
    CALL_STATUS = DebugState.OFF
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    def show_image_data(self, image_data):
        pass

class DebugDataFileHelper(BaseDebug):
    CALL_STATUS = DebugState.OFF
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    @can_call
    def file_and_directory(self, file_path, directory_exists, file_exists):
        statement = "File path: %s" % (file_path) + DebugCore.NEWLINE
        statement = statement + "Directory exist?: %s" % (directory_exists) + DebugCore.NEWLINE
        statement = statement + "File exist?: %s" % (file_exists) + DebugCore.NEWLINE
        self.debug_print(statement)

    @can_call
    def successful_file_and_directory_created(self, file_path):
        self.debug_print("File/Dir Created: (success) at %s" % (file_path))

class DebugPersistor(BaseDebug):
    CALL_STATUS = DebugState.OFF
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    @can_call
    def attempted_query(self, write_data, p_state):
        statement = "Query: (Attempt) (%s) %s" % (self._p_state(p_state), write_data)
        self.debug_print(statement)

    @can_call
    def successful_query(self, write_data, p_state, result):
        statement = "Query: (Success) (%s) (%s) %s" % (self._p_state(p_state), self._result(result), write_data)
        self.debug_print(statement)

    @can_call
    def attempted_written_data(self, write_data, p_state):
        statement = "Write: (Attempt) (%s) %s" % (self._p_state(p_state), write_data)
        self.debug_print(statement)

    @can_call
    def successful_written_data(self, write_data, p_state):
        statement = "Write: (Success) (%s) %s" % (self._p_state(p_state), write_data)
        self.debug_print(statement)

    def _p_state(self, p_state):
        if p_state:
            return "Persisted"
        else:
            return "Temporary"

    def _result(self, result):
        return result.name

class DebugPhotoFileFinder(BaseDebug):
    CALL_STATUS = DebugState.OFF
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    @can_call
    def print_all_photo_files_in_location(self, observed_photos):
        statement = ("Receipt location: %s" % GlobalVariables.RECEIPT_LOCATION) + DebugCore.NEWLINE
        statement = statement + self.list_to_string(observed_photos, 0) + DebugCore.NEWLINE
        self.debug_print(statement)

class DebugImageProcessor(BaseDebug):
    CALL_STATUS = DebugState.OFF
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
        statement = "The current photo is:" + image_location
        self.debug_print(statement)

    @can_call
    def show_set_attributes(self, attr, attr_value):
        self.debug_print("Set %s: %s" % (attr, attr_value))

    @can_call
    def text_and_relevant_text(self, original_text, relevant_text):
        statement_1 = "Original Text:" + DebugCore.NEWLINE
        statement_1 = statement_1 + self.indent_text(original_text)
        self.debug_print(statement_1)

        statement_2 = "Relevant text:" + self.dict_to_string(relevant_text) + DebugCore.NEWLINE
        self.debug_print(statement_2)

    @can_call
    def all_set_attributes(self, obj):
        statement = "Retriving attributes:"

        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            message = "Get %s: %s" % (attr, obj.__dict__[attr])
            statement = statement + self.text_tab(message, 1)

        self.debug_print(statement)

    @can_call
    def show_full_data(self, filled_data):
        statement = self.dict_to_string(filled_data)
        self.debug_print(statement)

class DebugImageData(BaseDebug):
    CALL_STATUS = DebugState.OFF
    VERBOSE_METHODS = []

    def __init__(self):
        pass

    @can_call
    def show_csv_text(self, joined_text):
        statement = "Data:" + joined_text
        self.debug_print(statement)
