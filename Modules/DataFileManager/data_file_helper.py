import os

from ..shared import GlobalVariables
from ..shared import GlobalConstants

LOCAL_DEBUG = False

def initialize_data_file():
    file_path = GlobalConstants.PERSISTED_DATA_PATH
    directory = os.path.dirname(file_path)

    directory_exists = os.path.exists(directory)
    file_exists = os.path.exists(file_path)

    if LOCAL_DEBUG:
        _debug_file_and_directory(directory_exists, file_exists)

    if not directory_exists:
        os.makedirs(directory)

    if not file_exists:
        open(GlobalConstants.PERSISTED_DATA_PATH, "w+").close()

    if LOCAL_DEBUG:
        _debug_successful_file_and_directory_created()

def clear_file():
    open(GlobalConstants.PERSISTED_DATA_PATH, 'w').close()

def does_file_exist():
    return os.path.isfile(GlobalConstants.PERSISTED_DATA_PATH)

def is_file_populated():
    return does_file_exist() or _file_size() > 0

def is_file_empty():
    return _file_size() == 0

def _file_size():
    return os.stat(GlobalConstants.PERSISTED_DATA_PATH).st_size

def _debug_file_and_directory(directory_exists, file_exists):
    print "file path: %s" % (file_path)
    print "does directory exist: %s" % (directory_exists)
    print "does file exist: %s" % (file_exists)

def _debug_successful_file_and_directory_created():
    print "file/dir successfully at %s" % (file_path)
