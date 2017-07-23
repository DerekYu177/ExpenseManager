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

        self.attr_list = []

        self.date = data["date"]
        self.time = data["time"]
        self.address = data["address"]
        self.total_amount = data["total_amount"]
        self.description = data["description"]

        if self.LOCAL_DEBUG:
            self.__debug_print_attributes()

    def as_csv_text(self):
        self.attr_list = [
            self.__date_time(),
            self.__shorten_address(),
            self.total_amount,
            self.description
        ]

        return ",".join(self.attr_list)

    def identifier(self):
        return self.__date_time()

    def __date_time(self):
        date = self.date.replace("/","")
        time = self.time

        return "%s-%s" % (date, time)

    def __shorten_address(self):
        if len(self.address) < self.MAX_ADDRESS_LENGTH: return self.address

        address = self.address[:self.MAX_ADDRESS_LENGTH-3]
        address = address + "..."

        return address

    def __debug_print_attributes(self):
        print "self.date: %s" % (self.date)
        print "self.time: %s" % (self.time)
        print "self.address: %s" % (self.address)
        print "self.total_amount: %s" % (self.total_amount)
        print "self.description: %s" % (self.description)
