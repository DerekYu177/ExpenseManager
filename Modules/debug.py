from shared import GlobalVariables
from shared import GlobalConstants

from image_data import Core

GLOBAL_DEBUG = False

def set_debug(debug_flag):
    GLOBAL_DEBUG = debug_flag
    DataFileHelper.LOCAL_DEBUG = debug_flag
    Persistor.LOCAL_DEBUG = debug_flag
    PhotoFileFinder.LOCAL_DEBUG = debug_flag
    ImageTextSearch.LOCAL_DEBUG = debug_flag

def show_sys_path():
    import sys
    for path in sys.path:
        print path

# TODO: this fomatting is shit

class DataFileHelper:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def file_and_directory(self, file_path, directory_exists, file_exists):
        print "file path: %s" % (file_path)
        print "does directory exist: %s" % (directory_exists)
        print "does file exist: %s" % (file_exists)

    def successful_file_and_directory_created(self, file_path):
        print "file/dir successfully at %s" % (file_path)

class Persistor:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def attempted_written_data(self, write_data):
        print "Data attempted to be written to file: %s" % (write_data)

    def successful_written_data(self, write_data):
        print "Data successfully written to file   : %s" % (write_data)

class PhotoFileFinder:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    # TODO: fix this formatting
    def print_all_photo_files_in_location(self, observed_photos):
        print   "All the photo files located in the receipt location %s are:"\
                "\n%s" % (
                    GlobalVariables.RECEIPT_LOCATION,
                    self.print_list_to_string(observed_photos)
                )


    def print_list_to_string(self, item_list):
        string = ""

        if type(item_list) is list:
            for item in item_list:
                string = string + item + "\n"
        else:
            string = item_list

        return string


class ImageTextSearch:
    LOCAL_DEBUG = False

    def __init__(self):
        pass

    def show_set_attributes(self, attr, attr_value):
        print "populate_core_data: setting %s as %s" % (attr, attr_value)

    def text_and_relevant_text(self, text, relevant_text):
        print "The original text was : %s" % (text)
        print "The relevant text was : %s" % (relevant_text)

    def append_original_text(self, text):
        return {
            "original text": text,
        }

    def all_set_attributes(self, obj):
        for attr in Core.ANALYSIS_ATTRIBUTES:
            print "%s has value %s" % (attr, obj.__dict__[attr])
