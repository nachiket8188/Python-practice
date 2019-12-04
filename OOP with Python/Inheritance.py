class Employee:

    raise_amount = 1.60
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # try using Employee.raise_amount


class Developer(Employee):
    raise_amount = 1.50

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees_managed = []
        else:
            self.employees_managed = employees

    def add_employee(self, emp):
        if emp not in self.employees_managed:
            self.employees_managed.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees_managed:
            self.employees_managed.remove(emp)

    def print_employees(self):
        for emp in self.employees_managed:
            print('-->', emp.fullname())


dev_1 = Developer('Nick','Totapholes', 16000, 'Python')
dev_2 = Developer('Nachiket','Palkandwar', 15050, 'R')

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr1 = Manager('Sue', 'Smith', 90000, [dev_1])
# print(mgr1.email)
# mgr1.add_employee(dev_2)
# print(mgr1.print_employees())
# print(isinstance(dev_1, Employee))
# print(isinstance(mgr1, Employee))
# print(isinstance(mgr1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))

