import datetime


class Employee:

    raise_amount = 1.60
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # try using Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True

emp_1 = Employee('Nick','Totapholes', 16000)
emp_2 = Employee('Nachiket','Palkandwar', 15050)
# print(Employee.num_of_emps)
#
# Employee.set_raise_amount(1.75)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# emp_str_1 = "John-Doe-7000"
# emp_str_2 = "Steve-Smith-17000"
# emp_str_3 = "Jane-Doe-8500"
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.first_name)
# print(new_emp_1.last_name)
# print(new_emp_1.email)
# print(new_emp_1.pay)
my_date = datetime.date(2019,11,27)
my_date2 = datetime.date(2019,12,1)
# print(Employee.is_workday(my_date))
print(Employee.is_workday(my_date2))
