#formatting

#putting {} then .format will place anything after in () inside of the curtly brackets through the format method
print('This is a string {}'.format('INSERT'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))

#this will reverse the order of the words because of the indexes placed inside of the curly brackets
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

#you can assign the strings inside of the format and place those variables inside of the curly brackets
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))