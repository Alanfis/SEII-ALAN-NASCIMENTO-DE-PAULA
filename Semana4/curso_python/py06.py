# Conditionals and Booleans: if, else, and elif statements

# Comparisons:
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identity: is 

# Booleans
# and
# or 
# not

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), []
    # Any empty mapping. For example, {}.

if True:
    print('Conditional was True')

if False:
    print('Conditional was True')

language = 'Python'

if language == 'Python':
    print('Conditional was true')

if language == 'Python':
    print('Language is Python')
else:
    print('No match')

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else: 
    print('No match')

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition_2 = None

if condition_2:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition_3 = 'Test'

if condition_3:
    print('Evaluated to True')
else:
    print('Evaluated to False')