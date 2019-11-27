# def hello_func():
#     # pass
#     print('Hello function!')
#
# print(hello_func)
# hello_func()

# def hello_func():
#     # pass
#     return 'Hello function!'
#
# print(hello_func())
# print(hello_func().upper())
#
# def hello_func(greet):
#     # pass
#     return f'Hello {greet}!'
#
# print(hello_func('Nick'))

# def student_info(*args, **kwargs):
#     print(args)  # positional arguments : these become a tuple
#     print(kwargs)  # keyword arguments : these become a dict
#
# student_info('Math', 'Art', name = 'John', age = 22)

# def student_info(*args, **kwargs):
#     print(args)  # positional arguments : these become a tuple
#     print(kwargs)  # keyword arguments : these become a dict

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}
#
# student_info(courses, info)
# student_info(*courses, **info)

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month.'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(is_leap(2017))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))