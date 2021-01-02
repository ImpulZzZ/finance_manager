import datetime


class Entry:
    def __init__(self, name, amount, monthly, yearly, date, last_date):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(amount, int)
        self.amount = amount
        assert isinstance(monthly, bool)
        self.monthly = monthly
        assert isinstance(yearly, bool)
        self.yearly = yearly
        assert isinstance(date, datetime.date)
        self.date = date
        assert isinstance(last_date, datetime.date)
        self.last_date = last_date

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_monthly(self):
        return self.monthly

    def set_monthly(self, monthly):
        self.monthly = monthly

    def get_yearly(self):
        return self.yearly

    def set_yearly(self, yearly):
        self.yearly = yearly

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_last_date(self):
        return self.last_date

    def set_last_date(self, last_date):
        self.last_date = last_date
