# Lists, Tuples and Sets

courses = ['History', 'Math', 'Physics', 'CompSci'] # list

sorted_courses = sorted(courses)
print(sorted_courses)
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art') # Adicionar string na lista
print(courses)
courses.insert(0, 'Art')
print(courses)

courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)

print(courses)
print(courses[0])

courses.extend(courses_2)
print(courses)

courses.remove('Math')
print(courses)

courses.pop()
print(courses)

popped = courses.pop()
print(popped)

courses.reverse()
print(courses)

#courses.sort()
#print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses.index('CompSci'))
print('Art' in courses)

for item in courses:
    print(item)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses_3 = ['History_3', 'Math_3', 'Physics_3', 'CompSci_3']

courses_3str = ','.join(courses_3)
print(courses_3str)

new_list = courses_3str.split(' - ')
print(new_list)

# Tuples

# Mutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty list
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = {}
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()