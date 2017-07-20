from shared import global_variables
from shared import global_constants

import os

class DataFileHelper:

    def initialize_data_file(self):
        self.file_path = global_constants.PERSISTED_DATA_PATH
        directory = os.path.dirname(self.file_path)

        directory_exists = os.path.exists(directory)
        file_exists = os.path.exists(self.file_path)

        if global_variables.DEBUG:
            self.__debug_file_and_directory(directory_exists, file_exists)

        if not directory_exists:
            os.makedirs(directory)

        if not file_exists:
            open(global_constants.PERSISTED_DATA_PATH, "w+").close()

        if global_variables.DEBUG:
            self.__debug_successful_file_and_directory_created()

    def clear_file(self):
        open(global_constants.PERSISTED_DATA_PATH, 'w').close()

    def does_file_exist(self):
        return os.path.isfile(global_constants.PERSISTED_DATA_PATH)

    def is_file_populated(self):
        return self.does_file_exist() or self.__file_size() > 0

    def is_file_empty(self):
        return self.__file_size() == 0

    def __file_size(self):
        return os.stat(global_constants.PERSISTED_DATA_PATH).st_size

    def __debug_file_and_directory(self, directory_exists, file_exists):
        print "file path: %s" % (self.file_path)
        print "does directory exist: %s" % (directory_exists)
        print "does file exist: %s" % (file_exists)

    def __debug_successful_file_and_directory_created(self):
        print "file/dir successfully at %s" % (self.file_path)
