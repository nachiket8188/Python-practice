class Employee():
    raise_amt = 1.25

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapany.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Corey', 'Schafer', 15000)
emp2 = Employee('Test', 'Employee' , 21000)

# print(emp1)
# print(repr(emp1))
# print(str(emp1))

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a',"b"))
#
# print(emp1 + emp2)
print(len("Test"))
print('Test'.__len__())
print(len(emp2))