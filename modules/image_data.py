from collections import OrderedDict
from enum import Enum

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
        ("date", 0),
        ("time", 0),
        ("address", 1),
        ("total_amount", 0),
        ("description", 2)
    ])

class ImageData(object):
    MAX_ADDRESS_LENGTH = 10
    EMPTY = "-"

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

    def __str__(self):
        self._normalize_none()
        return ",".join(self.attr_list)

    def exists_in_block_of_text(self, text):
        return Finder(self.attr_list[0], self.attr_list[1]).exists_in_block_of_text(text)

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
        build_results = []

        build_results = self._build_using_builder_attributes(build_results)
        build_results = self._query_for_required_values(build_results)

        return build_results

    def _build_using_builder_attributes(self, build_results):
        for attribute_name, value in Attributes.BUILDER_ATTRIBUTES.items():
            attribute = getattr(self, attribute_name)
            if attribute is None:
                build_results.append(self.EMPTY)
            else:
                function = getattr(self, self._privatize(attribute_name))
                build_results.append(function())

        return build_results

    def _query_for_required_values(self, build_results):
        for index, attribute_name in enumerate(Attributes.BUILDER_ATTRIBUTES):
            value = Attributes.BUILDER_ATTRIBUTES[attribute_name]

            if self._required(value) and build_results[index] is None:
                build_results[index] = self._query(attribute_name)

        return build_results

    def _date(self):
        return self.date.replace("/","")

    def _time(self):
        hours, minutes, seconds = self.time.split(":")
        military_time = hours + minutes
        return "%s(%s)" % (military_time, seconds)

    def _address(self):
        return self._shorten_addr(self.address)

    def _total_amount(self):
        return self.total_amount

    def _description(self):
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

class Finder(ImageData):
    def __init__(self, date, time):
        self.identifier = (date, time)

    def exists_in_block_of_text(self, block_of_text):
        date, time = self.identifier
        if date is self.EMPTY or time is self.EMPTY:
            # we don't want to write None
            return ExistanceState.NONE

        for row in block_of_text:
            if row[0] == date and row[1] == time:
                return ExistanceState.EXISTS

        return ExistanceState.NEW_ENTRY

class ExistanceState(Enum):
    NEW_ENTRY = 0
    EXISTS = 1
    NONE = 2
