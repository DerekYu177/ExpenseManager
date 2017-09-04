import shared

class Query(object):
    DEFAULT_MESSAGE = None

    def query_user(self, query_message):
        if shared.GlobalVariables.STATE is shared.State.NOMINAL:
            return raw_input(query_message)
        else:
            return self.DEFAULT_MESSAGE

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
