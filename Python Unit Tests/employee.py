import requests


class Employee:
    """A sample Employee class"""
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # try using Employee.raise_amount

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{}/{}".format(self.last_name, month))
        if response.ok:
            return response.text
        else:
            return "Bad response!"
