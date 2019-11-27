class Employee:

    raise_amount = 1.04
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

print(Employee.num_of_emps)

emp_1 = Employee('Nick','Totapholes', 16000)
emp_2 = Employee('Nachiket','Palkandwar', 15050)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__ )  # doesn't return raise_amount attribute as it is a class attribute
# print(Employee.__dict__)  # this will return a raise_amount class attribute

# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)