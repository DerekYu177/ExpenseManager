# from image_data import ImageData
from debug import DebugCore
from debug import DebugState

class Query(object):
    DEFAULT_MESSAGE = "dank inputs"

    def query_user(self, query_message):
        if DebugCore.GLOBAL_DEBUG is DebugState.OFF:
            return raw_input(query_message)
        else:
            return self.DEFAULT_MESSAGE

class QueryForAdditionalDetails(Query):
    CUSTOM_QUERY = {
        "address": "Do you remember the address for this purchase?",
        "description": "Add a description to your purchase"
    }

    def __init__(self, image_data, query_attribute, image_name):
        self.image_name = image_name
        self.image_data = image_data
        self.query_attribute = query_attribute

    def query(self):
        return self.query_user(
            self._query_message() +
            self.CUSTOM_QUERY[self.query_attribute]
        )

    def _query_message(self):
        return """We were unable to determine the %s from the image %s.
        On the date %s, at %s, you spent %s.""" % (
            self.query_attribute,
            self.image_name,
            self.image_data.date,
            self.image_data.time,
            self.image_data.total_amount
        )
