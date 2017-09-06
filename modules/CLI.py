import shared

class PrintCore:
    MESSAGE_COUNTER = 0
    MAX_MESSAGE_LENGTH = 100
    VERBOSE_METHODS = True # FIXME
    NEWLINE = "\n"

class Printer:
    def show(self, source, message):
        message = self.message_truncate(message)
        print "%s:(%s):%s" % (PrintCore.MESSAGE_COUNTER, source, message)
        PrintCore.MESSAGE_COUNTER = PrintCore.MESSAGE_COUNTER + 1

    def message_truncate(self, text):
        if PrintCore.VERBOSE_METHODS or len(text) < PrintCore.MAX_MESSAGE_LENGTH: # FIXME
            return text

        text = text[:PrintCore.MAX_MESSAGE_LENGTH-3]
        text = text + "..."
        return text

    def message_truncate_access_location(self, location):
        return location # TODO

    def text_tab(self, text, tab):
        space_number = tab * 3
        space = " "
        return space_number * space + text

    def indent_text(self, text, current_indentation=0):
        statement = PrintCore.NEWLINE
        for line in text.split(PrintCore.NEWLINE):
            statement = statement + self.text_tab(line, current_indentation + 1) + PrintCore.NEWLINE
        return statement

    def list_to_string(self, item_in_list, current_indentation=0):
        statement = PrintCore.NEWLINE
        for item in item_in_list:
            statement = statement + self.text_tab(item, current_indentation + 1) + PrintCore.NEWLINE
        return statement

    def dict_to_string(self, dictionary, current_indentation=0):
        statement = PrintCore.NEWLINE
        for key, value in dictionary.items():
            item = "%s:%s" % (key, value)
            statement = statement + self.text_tab(item, current_indentation + 1) + PrintCore.NEWLINE
        return statement

class Query(object):
    DEFAULT_MESSAGE = None

    def query_user(self, query_message):
        if shared.GlobalVariables.STATE is shared.State.NOMINAL:
            return raw_input(query_message)
        else:
            return self.DEFAULT_MESSAGE

    def location(self):
        import Tkinter as tk
        from tkFileDialog import askdirectory

        if shared.GlobalVariables.STATE is shared.State.NOMINAL:
            tk_prompt = tk.Tk()
            tk_prompt.withdraw()
            return askdirectory()
        else:
            return shared.GlobalVariables.IMAGE_LOCATION

class QueryForAdditionalDetails(Query):
    CUSTOM_QUERY = {
        "address": "Do you remember the address for this purchase?",
        "description": "Add a description to your purchase"
    }
    RUDE_QUERY = "Just do the thing"

    def __init__(self, image_data, query_attribute, image_name):
        self.image_name = image_name
        self.image_data = image_data
        self.query_attribute = query_attribute

    def query(self):
        return self.query_user(
            self._query_message() +
            self._custom_query_message()
        )

    def _custom_query_message(self):
        if self.query_attribute in self.CUSTOM_QUERY.keys():
            return self.CUSTOM_QUERY[self.query_attribute]
        else:
            return self.RUDE_QUERY

    def _query_message(self):
        return """We were unable to determine the %s from the image %s.
        On the date %s, at %s, you spent %s.""" % (
            self.query_attribute,
            self.image_name,
            self.image_data.date or self.DEFAULT_MESSAGE,
            self.image_data.time or self.DEFAULT_MESSAGE,
            self.image_data.total_amount or self.DEFAULT_MESSAGE
        )
