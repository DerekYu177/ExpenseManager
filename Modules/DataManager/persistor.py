from shared import GlobalVariables
from shared import GlobalConstants

import csv
import os

class Persistor:

    def __init__(self):
        # assume that the file exists
        pass

    def persist(self, write_data):
        data_file = open(GlobalConstants.PERSISTED_DATA_PATH, "a") #append

        if GlobalVariables.DEBUG:
            self.__debug_attempted_written_data(write_data)

        write_data_with_newline = write_data.as_csv_text() + "\n"
        data_file.write(write_data_with_newline)

        if GlobalVariables.DEBUG:
            self.__debug_successful_written_data(write_data)

        data_file.close()

    def does_data_exist(self, new_data):
        identifier = new_data.identifier()

        with open(GlobalConstants.PERSISTED_DATA_PATH, "r") as f: #read only
            reader = csv.reader(f, delimiter=",")
            for row in reader: # O(N) scability
                if row[0] == identifier: # sort by time
                    f.close()
                    return True

            f.close()
            return False

    def __debug_attempted_written_data(self, write_data):
        print "Data attempted to be written to file: %s" % (write_data)

    def __debug_successful_written_data(self, write_data):
        print "Data successfully written to file   : %s" % (write_data)
