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


dev_1 = Employee('Nick','Totapholes', 16000)
dev_2 = Employee('Nachiket','Palkandwar', 15050)
