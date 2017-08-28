from shared import ImageDataCore
from debug import DebugImageData as debug
debug = debug()

class ImageData:

    MAX_ADDRESS_LENGTH = 10
    LOCAL_DEBUG = False

    def __init__(self, data):

        # data = {
        #     "date": data["date"],
        #     "time": data["time"],
        #     "address": data["address"],
        #     "total_amount": data["total_amount"],
        #     "description": data["description"]
        # }

        self.raw_data = data
        self._assign_instance_variables()

    def is_valid(self):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            if (attr in ImageDataCore.PROCESSED_ATTRIBUTES) and (self.raw_data[attr] is None):
                return False

        return True

    def as_csv_text(self):
        self.attr_list = self._set_text()
        self._normalize_none()
        text = ",".join(self.attr_list)
        return text

    def identifier(self):
        return self._date_time()

    def _set_text(self):
        return [
            self._date_time(),
            self._address(),
            self.total_amount,
            self._description()
        ]

    def _assign_instance_variables(self):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, self.raw_data[attr])

    def _date_time(self):
        if self.date is None:
            return None

        date = self.date.replace("/","")
        time = self.time

        return "%s-%s" % (date, time)

    def _description(self):
        if self.description is None:
            return None

        return self.description

    def _address(self):
        if self.address is None:
            return None

        return self._shorten(self.address)

    def _shorten(self, address):
        if len(address) < self.MAX_ADDRESS_LENGTH:
            return address

        address = address[:self.MAX_ADDRESS_LENGTH-3]
        address = address + "..."

        return address

    def _normalize_none(self):
        for pos, attr in enumerate(self.attr_list):
            if attr is None:
                self.attr_list[pos] = str(None)
