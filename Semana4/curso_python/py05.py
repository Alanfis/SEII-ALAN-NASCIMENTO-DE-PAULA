# Dictionaries: Working with Key-Value Pairs

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['courses'])

student_2 = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student_2['phone'] = '555-5555'
student_2['name'] = 'Jane'
print(student_2)
print(student_2.get('name'))
print(student_2.get('phone', 'Not Found'))

student.update({'name': 'Jane_2', 'age': 26, 'phone': '5555-5555'})
print(student)

del student['age']
print(student) 

age = student_2.pop('age')
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)