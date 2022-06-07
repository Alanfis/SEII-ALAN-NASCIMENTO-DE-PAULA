# Strigs: Working with Textual Data


message = 'Hello World'
message2 = "Bobby's World"
new_message = message.replace('World', 'Universe')

greeting = 'Hello'
name = 'Michael'

message3 = greeting + ',' + name + '. Welcome!'

message4 = '{}, {}. Welcome!'.format(greeting, name)

message5 = f'{greeting}, {name.upper()}. Welcome!'

print(message)
print(message[0])
print(message[0:5]) 
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))
print(message3)
print(message4)
print(message5)
print(dir(name))
print(help(str))
print(help(str.lower))
print(len(message))
print(new_message)
print(message2)
