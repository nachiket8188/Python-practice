student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['phone_no'] = '571-549-9869'

print(student)
print(student['courses'])
print(student.get('courses'))
print(student.get('phone', 'Not found.'))
print(student.get('phone_no', 'Not found.'))

student.update({'name': 'Jane', 'age': 31})
print(student)
# del student['age']
print(student)
age = student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for k,v in student.items():
    print(k, v)
