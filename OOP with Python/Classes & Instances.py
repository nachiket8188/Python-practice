
class Employee:
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'


# emp_1 = Employee()
# emp_2 = Employee()
# print(emp_1)
# print(emp_2)

emp_1 = Employee('Nick','Totapholes', 16000)
emp_2 = Employee('Nachiket','Palkandwar', 15050)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())
print()
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
