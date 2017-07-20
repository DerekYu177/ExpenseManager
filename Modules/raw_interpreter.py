from shared import global_variables

class RawInterpreter:
    MAX_ADDRESS_LENGTH = 10

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

        if global_variables.DEBUG:
            self.__debug_print_attributes()

    def interpret(self):
        self.attr_list = [
            self.date_time(),
            self.short_address(),
            self.total_amount,
            self.description
        ]

        return ",".join(self.attr_list)

    def date_time(self):
        date = self.date.replace("\'","")
        time = self.time.replace("\:", "")

        return "%s-%s" % (date, time)

    def short_address(self):
        if len(self.address) < self.MAX_ADDRESS_LENGTH: return self.address

        address = self.address[:self.MAX_ADDRESS_LENGTH-3]
        address = address + "..."

        print address
        return address

    def __debug_print_attributes(self):
        print "self.date: %s" % (self.date)
        print "self.time: %s" % (self.time)
        print "self.address: %s" % (self.address)
        print "self.total_amount: %s" % (self.total_amount)
        print "self.description: %s" % (self.description)
