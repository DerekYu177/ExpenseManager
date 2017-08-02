class Core:
    ANALYSIS_ATTRIBUTES = [
        "date",
        "time",
        "address",
        "total_amount",
        "description"
    ]

    PROCESSED_ATTRIBUTES = [
        "date",
        "time",
        "total_amount"
    ]

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

    def as_csv_text(self):
        self._set_text
        self._normalize_none()

        text = ",".join(self.attr_list)
        debug.show_csv_text(text)
        return text

    def identifier(self):
        return self._date_time()

    def _set_text(self):
        self.attr_list = [
            self._date_time(),
            self._shorten_address(),
            self.total_amount,
            self.description
        ]

    def _assign_instance_variables(self):
        for attr in Core.ANALYSIS_ATTRIBUTES:
            setattr(self, attr, self.raw_data[attr])

    def _date_time(self):
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
        for attr, position in enumerate(self.attr_list):
            if attr is None:
                self.attr_list[position] = "None"

    def _debug_print_attributes(self):
        print "self.date: %s" % (self.date)
        print "self.time: %s" % (self.time)
        print "self.address: %s" % (self.address)
        print "self.total_amount: %s" % (self.total_amount)
        print "self.description: %s" % (self.description)
