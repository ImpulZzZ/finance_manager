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

    # evaluate entry and return calculated value
    def calculate(self, checkboxes, from_date, to_date):

        costs = 0
        savings = 0

        # evaluate whether paydate for unique costs is in interval or not
        if not self.monthly and not self.yearly:
            if checkboxes["from_date"]:
                if self.date.year           < from_date["year"]:
                    if self.date.month      < from_date["month"]:
                        return (0, 0)

            if checkboxes["to_date"]:
                if self.date.year           > to_date["year"]:
                    if self.date.month      > to_date["month"]:
                        return (0, 0)


        if checkboxes["yearly"]:
            if self.yearly:
                if checkboxes["yearly_to_monthly"]:
                    costs = costs + (self.amount / 12)
                else:
                    costs = costs + self.amount
                savings = savings + (self.amount / 12)
        if checkboxes["monthly"]:
            if self.monthly:
                costs = costs + self.amount
        if checkboxes["once"]:
            if not self.yearly and not self.monthly:
                costs = costs + self.amount

        return (costs, savings)