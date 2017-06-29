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
            print "file path: %s" % (self.file_path)
            print "does directory exist: %s" % (directory_exists)
            print "does file exist: %s" % (file_exists)

        if not directory_exists:
            os.makedirs(directory)

        if not file_exists:
            open(global_constants.PERSISTED_DATA_PATH, "w+").close()

        return

    def persist(self, data):
        data_file = open(global_constants.PERSISTED_DATA_PATH, "a") #append
        write_data = self.array_to_string(data)

        if global_variables.DEBUG:
            print write_data

        write_data_with_newline = write_data + "\n"
        data_file.write(write_data_with_newline)
        data_file.close()

    def find_data(self, data):
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

    def array_to_string(self, arr):
        try:
            return ",".join(arr)
        except TypeError:
            print "Data format should be in a list"

    def is_file_empty():
        return os.stat(global_constants.PERSISTED_DATA_PATH).st_size == 0
