# Functions

def hello_func():
    print('Hello Function!')
    
hello_func()
print('Hello Function!')

def hello_func2():
    return 'Hello Function 2.'

print(hello_func2())

print(hello_func2().upper())

def hello_func3(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func3('Hi', name = 'Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

student_info('Math', 'Art', name='John', age=22)

# Number of days per month. First value placeholder for indexing purposes.

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year"""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(days_in_month(2017, 2))
