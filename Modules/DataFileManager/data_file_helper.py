import os

from ..shared import GlobalVariables
from ..shared import GlobalConstants
from ..debug import DebugDataFileHelper as debug

debug = debug()

def initialize_data_file():
    file_path = GlobalConstants.PERSISTED_DATA_PATH
    directory = os.path.dirname(file_path)

    directory_exists = os.path.exists(directory)
    file_exists = os.path.exists(file_path)

    if debug.LOCAL_DEBUG:
        debug.file_and_directory(file_path, directory_exists, file_exists)

    if not directory_exists:
        os.makedirs(directory)

    if not file_exists:
        open(GlobalConstants.PERSISTED_DATA_PATH, "w+").close()

    if debug.LOCAL_DEBUG:
        debug.successful_file_and_directory_created(file_path)

def clear_file():
    open(GlobalConstants.PERSISTED_DATA_PATH, 'w').close()

def del_file():
    os.remove(GlobalConstants.PERSISTED_DATA_PATH)

def does_file_exist():
    return os.path.isfile(GlobalConstants.PERSISTED_DATA_PATH)

def is_file_populated():
    return does_file_exist() and _file_size() > 0

def is_file_empty():
    return _file_size() == 0

def _file_size():
    return os.stat(GlobalConstants.PERSISTED_DATA_PATH).st_size
