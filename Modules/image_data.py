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

        if self.LOCAL_DEBUG:
            self._debug_print_attributes()

    def is_valid(self):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            if (attr in ImageDataCore.PROCESSED_ATTRIBUTES) and (self.raw_data[attr] is None):
                return False

        return True

    def as_csv_text(self):
        self.attr_list = self._set_text()
        self._normalize_none()

        print "DEBUG: self.attr_list: %s" % (self.attr_list)
        text = ",".join(self.attr_list)
        debug.show_csv_text(text)
        return text

    def identifier(self):
        return self._date_time()

    def _set_text(self):
        return [
            self._date_time(),
            self._shorten_address(),
            self.total_amount,
            self.description
        ]

    def _assign_instance_variables(self):
        for attr in ImageDataCore.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, self.raw_data[attr])

    def _date_time(self):
        if self.date is None: return self.date

        date = self.date.replace("/","")
        time = self.time

        return "%s-%s" % (date, time)

    def _shorten_address(self):
        if self.address is None: return self.address

        if len(self.address) < self.MAX_ADDRESS_LENGTH: return self.address

        address = self.address[:self.MAX_ADDRESS_LENGTH-3]
        address = address + "..."

        return address

    def _normalize_none(self):
        for pos, attr in enumerate(self.attr_list):
            if attr is None:
                self.attr_list[pos] = str(None)

    def _debug_print_attributes(self):
        print "self.date: %s" % (self.date)
        print "self.time: %s" % (self.time)
        print "self.address: %s" % (self.address)
        print "self.total_amount: %s" % (self.total_amount)
        print "self.description: %s" % (self.description)
