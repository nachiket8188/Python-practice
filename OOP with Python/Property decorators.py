class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):  # although we're defining email() in our class like it's a method, but we're able to access it
        # like an attribute down below.
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print("Delete name !")
        self.first = None
        self.last = None

emp1 = Employee('John', 'Smith')

# emp1.first = 'Jim'  # problem here but no error thrown
emp1.fullname = 'Nick Palkandwar'  # problem here, throws error

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.first)
