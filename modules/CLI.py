from image_data import ImageData
from debug import DebugCore

class Query(object):
    DEFAULT_MESSAGE = "dank inputs"

    def query_user(query_message):
        if DebugCore.GLOBAL_DEBUG is DebugState.OFF:
            return raw_input(query_message)
        else:
            return self.DEFAULT_MESSAGE


class QueryForAdditionalDetails(ImageData, Query):
    CUSTOM_QUERY = {
        "address": "Do you remember the address for this purchase?",
        "description": "Add a description to your purchase"
    }

    def __init__(self, imagedata_superklass, query_attribute):
        self.imagedata_superklass = imagedata_superklass
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
            self.imagedata_superklass.image_name,
            self.imagedata_superklass.date,
            self.imagedata_superklass.time,
            self.imagedata_superklass.total_amount
        )
