from collections import OrderedDict

import shared
from debug import DebugImageData as debug
from CLI import QueryForAdditionalDetails
debug = debug()

class Attributes:
    PROCESSED_ATTRIBUTES = [
        "date",
        "time",
        "total_amount"
    ]

    UNCERTAIN_ATTRIBUTES = [
        "address",
        "description"
    ]

    ANALYSIS_ATTRIBUTES = PROCESSED_ATTRIBUTES + UNCERTAIN_ATTRIBUTES

    BUILDER_ATTRIBUTES = OrderedDict([
        ("date_time", 0),
        ("address", 1),
        ("total_amount", 0),
        ("description", 2)
    ])

class ImageData(object):
    MAX_ADDRESS_LENGTH = 10

    def __init__(self, data, image_name):

        # data = {
        #     "date": data["date"],
        #     "time": data["time"],
        #     "address": data["address"],
        #     "total_amount": data["total_amount"],
        #     "description": data["description"]
        # }

        self.image_name = image_name
        self.raw_data = data
        self.attr_list = Builder(self.raw_data, self.image_name).process()

    def is_valid(self):
        for attr in Attributes.ANALYSIS_ATTRIBUTES:
            if (attr in Attributes.PROCESSED_ATTRIBUTES) and (self.raw_data[attr] is None):
                return False

        return True

    def __str__(self):
        self._normalize_none()
        text = ",".join(self.attr_list)
        return text

    def identifier(self):
        return self.attr_list[0]

    def _assign_instance_variables(self):
        for attr in Attributes.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, self.raw_data[attr])

    def _normalize_none(self):
        for pos, attr in enumerate(self.attr_list):
            if attr is None:
                self.attr_list[pos] = str(None)

    def _query(self, query_attribute):
        return QueryForAdditionalDetails(self, query_attribute, self.image_name).query()

class Builder(ImageData):
    def __init__(self, data, image_name):
        self.image_name = image_name
        for attr in Attributes.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, data[attr])

    def process(self):
        self.build_results = []

        self._build_using_builder_attributes()
        self._query_for_required_values()

        return self.build_results

    def _build_using_builder_attributes(self):
        for attribute_name, value in Attributes.BUILDER_ATTRIBUTES.items():
            function = getattr(self, self._privatize(attribute_name))
            self.build_results.append(function())

    def _query_for_required_values(self):
        for index, attribute_name in enumerate(Attributes.BUILDER_ATTRIBUTES):
            value = Attributes.BUILDER_ATTRIBUTES[attribute_name]

            if self._required(value) and self.build_results[index] is None:
                self.build_results[index] = self._query(attribute_name)

    def _date_time(self):
        if self.date is None:
            return None

        date = self.date.replace("/","")
        time = self.time

        return "%s-%s" % (date, time)

    def _address(self):
        if self.address is None:
            return None

        return self._shorten_addr(self.address)

    def _total_amount(self):
        if self.total_amount is None:
            return None

        return self.total_amount

    def _description(self):
        if self.description is None:
            return None

        return self.description

    def _required(self, value):
        if shared.GlobalVariables.PRECISION is shared.BuilderRequirements.REQUIRES_COMPLETE:
            return True

        return value == shared.GlobalVariables.PRECISION.value

    def _privatize(self, method_name):
        return "_" + method_name

    def _shorten_addr(self, address):
        if len(address) < self.MAX_ADDRESS_LENGTH:
            return address

        address = address[:self.MAX_ADDRESS_LENGTH-3]
        address = address + "..."

        return address
