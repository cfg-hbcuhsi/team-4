import datetime


class Entry:
    def __init__(self, name, value, category, date):
        self.name = name
        self.value = value
        self.category = category
        self.date = date

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def set_category(self, category):
        self.category = category

    def set_date(self, date):
        self.date = date

    def print_entry(self):
        msg = '' + self.name + ' ' + str(self.value) + ' ' + self.category + ' ' + str(self.date)
        return msg

    def get_day(self):
        splice = str(self.date).split('-')
        return splice[2]

    def get_month(self):
        splice = str(self.date).split('-')
        return splice[1]

    def get_year(self):
        splice = str(self.date).split('-')
        return splice[0]
