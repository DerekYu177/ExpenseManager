from enum import Enum

from shared import ImageDataCore
from shared import ImageDataBuilder
from shared import BuilderRequirements
from debug import DebugImageData as debug
debug = debug()

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
        self.attr_list = Builder(self.raw_data).process()

    def is_valid(self):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            if (attr in ImageDataCore.PROCESSED_ATTRIBUTES) and (self.raw_data[attr] is None):
                return False

        return True

    def as_csv_text(self):
        self._normalize_none()
        text = ",".join(self.attr_list)
        return text

    def identifier(self):
        return self.attr_list[0]

    def _assign_instance_variables(self):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, self.raw_data[attr])

    def _normalize_none(self):
        for pos, attr in enumerate(self.attr_list):
            if attr is None:
                self.attr_list[pos] = str(None)

    def _query(self, query_attribute):
        QueryForAdditionalDetails(self, query_attribute).query()

class Builder(ImageData):
    SUBSTITUTE = "HIT"

    def __init__(self, data):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, data[attr])

    def process(self):
        self._build_using_builder_attributes()
        self._query_for_required_values()

        return self.build_results

    def _build_using_builder_attributes(self):
        self.build_results = []

        for attribute_name, value in ImageDataBuilder.BUILDER_ATTRIBUTES.items():
            function = getattr(self, self._privatize(attribute_name))
            self.build_results.append(function())

    def _query_for_required_values(self):
        for index, attribute_name in enumerate(ImageDataBuilder.BUILDER_ATTRIBUTES):
            value = ImageDataBuilder.BUILDER_ATTRIBUTES[attribute_name]

            if self._required(value) and self.build_results[index] is None:
                self.build_results[index] = self.SUBSTITUTE

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
        if ImageDataBuilder.PRECISION is BuilderRequirements.REQUIRES_COMPLETE:
            return True

        return value == ImageDataBuilder.PRECISION.value

    def _privatize(self, method_name):
        return "_" + method_name

    def _shorten_addr(self, address):
        if len(address) < self.MAX_ADDRESS_LENGTH:
            return address

        address = address[:self.MAX_ADDRESS_LENGTH-3]
        address = address + "..."

        return address
