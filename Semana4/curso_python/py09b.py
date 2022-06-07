# Import Modules and Exploring The Standard Library

import sys
# sys.path.append() diretório do módulo 
import random
import math
import datetime
import calendar
import os
import antigravity
from py09 import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
random_course = random.choice(courses)

rads = math.radians(90)
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(random_course)
print(index)
print(test)

print(sys.path)

print(math.sin(rads))

#print(os.getcwd())

print(os.__file__)