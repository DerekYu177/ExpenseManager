from shared import global_variables as global_variables
from shared import global_constants as global_constants
import csv, os

class Persistor:

    def __init__(self):
        self.initialize_data_file()

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

        return

    def persist(self, data):
        data_file = open(global_constants.PERSISTED_DATA_PATH, "a") #append
        write_data = self.__array_to_string(data)

        if global_variables.DEBUG:
            self.__debug_attempted_written_data(write_data)

        write_data_with_newline = write_data + "\n"
        data_file.write(write_data_with_newline)

        if global_variables.DEBUG:
            self.__debug_successful_written_data(write_data)

        data_file.close()

    def does_data_exist(self, data):
        with open(global_constants.PERSISTED_DATA_PATH, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if data[1] == row[1]: # sort by time
                    f.close()
                    return True

            f.close()
            return False

    def clear_file(self):
        open(global_constants.PERSISTED_DATA_PATH, 'w').close()

    def is_file_empty(self):
        return os.stat(global_constants.PERSISTED_DATA_PATH).st_size == 0

    def __array_to_string(self, arr):
        try:
            return ",".join(arr)
        except TypeError:
            print "Data format should be in a list"

    def __debug_file_and_directory(self, directory_exists, file_exists):
        print "file path: %s" % (self.file_path)
        print "does directory exist: %s" % (directory_exists)
        print "does file exist: %s" % (file_exists)

    def __debug_attempted_written_data(self, write_data):
        print "Data attempted to be written to file: %s" % (write_data)

    def __debug_successful_written_data(self, write_data):
        print "Data successfully written to file   : %s" % (write_data)

    def __debug_successful_file_and_directory_created(self):
        print "file/dir successfully at %s" % (self.file_path)
