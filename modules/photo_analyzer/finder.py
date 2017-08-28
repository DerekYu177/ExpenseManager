import re

class Finder(object): # new class structure here
    def __init__(self, text):
        self.text = text

    def find(self, regex):
        match = re.findall(regex, self.text)

        if not match:
            return None
        elif len(match) == 1:
            return match[0]
        else:
            return match

    def define_finders(self, attr):
        return "find_%s" % (attr)

    def find_date(self):
        return DateFinder(self.text).find_date()

    def find_time(self):
        time_regex = r'(\d+:\d+:\d+)'
        return self.find(time_regex)

    def find_address(self):
        return None # TODO

    def find_total_amount(self):
        return MoneyFinder(self.text).find_total_amount()

    def find_description(self):
        return None # TODO

class MoneyFinder(Finder):
    regex = r'[$]\s*\d+\.\d{2}'

    def find_total_amount(self):
        amounts = super(MoneyFinder, self).find(self.regex)
        return self._max_amounts(amounts)

    def _max_amounts(self, money_list):
        if money_list is None:
            return None

        if type(money_list) is str:
            return money_list

        if type(money_list) is list:
            return self._max_list_finder(money_list)

    def _max_list_finder(self, money_list):
        max_amount = 0

        for money in money_list:
            m = self._strip_dollar_sign(money)

            if m > max_amount:
                max_amount = m

        return self._add_dollar_sign(max_amount)

    def _strip_dollar_sign(self, money):
        if money[0] != "$":
            return

        return float(money[1:])

    def _add_dollar_sign(self, number):
        number = str(number)

        number = self._add_lost_zero(number)

        return "$" + number

    def _add_lost_zero(self, number):
        dollar, cents = number.split('.')

        if len(cents) == 0:
            return number + "00"
        elif len(cents) == 1:
            return number + "0"
        else:
            return number

class DateFinder(Finder):
    regex = r'(\d+/\d+/\d+)'
    identifier = separator = "/"
    MAX_MONTH = 12
    year_range = 1

    def find_date(self):
        raw_date = super(DateFinder, self).find(self.regex)

        if raw_date is None:
            return None

        return self._day_month_year(raw_date)

    def _day_month_year(self, date):
        day, month, year = date.split(self.identifier)
        day, month, year = self._sanitize_date_data(day, month, year)
        day, month, year = self._format_date(day, month, year)
        return day + self.separator + month + self.separator + year

    def _sanitize_date_data(self, day, month, year):
        year = self._full_year(year)
        day, month = self._sanitize_day_month(day, month)
        return day, month, year

    def _full_year(self, year):
        if len(year) == 2:
            return int("20" + year)
        else:
            return int(year)

    def _sanitize_day_month(self, day, month):
        day = int(day)
        month = int(month)

        if (month > self.MAX_MONTH):
            month, day = day, month

        return day, month

    def _format_date(self, day, month, year):
        day = self._format_full_length(day)
        month = self._format_full_length(month)
        return str(day), str(month), str(year)

    def _format_full_length(self, unit):
        unit = str(unit)
        if len(unit) <= 1:
            return "0" + unit
        else:
            return unit
