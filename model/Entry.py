import datetime


class Entry:
    def __init__(self, name, description, amount, weekly, yearly, date):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(description, str)
        self.description = description
        assert isinstance(amount, int)
        self.amount = amount
        assert isinstance(weekly, bool)
        self.weekly = weekly
        assert isinstance(yearly, bool)
        self.yearly = yearly
        assert isinstance(date, datetime.date)
        self.date = date

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_weekly(self):
        return self.weekly

    def set_weekly(self, weekly):
        self.weekly = weekly

    def get_yearly(self):
        return self.yearly

    def set_yearly(self, yearly):
        self.yearly = yearly

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date
