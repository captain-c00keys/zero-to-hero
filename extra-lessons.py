#formatting

#putting {} then .format will place anything after in () inside of the curtly brackets through the format method
print('This is a string {}'.format('INSERT'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))

#this will reverse the order of the words because of the indexes placed inside of the curly brackets
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

#you can assign the strings inside of the format and place those variables inside of the curly brackets
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/888

#{r:1.5f} the r is the variable inside of format, the 1 is the amount of whitespace, and the 3f is how many places
# after the period
print("The result was {r:1.3f}".format(r=result))

#ex

name = "jose"
print('Hello, his name is {}'.format(name))

#displays the same as above. It's called f string literals
print(f'Hello, his name is {name}')
