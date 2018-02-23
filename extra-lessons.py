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

#putting an element into a list
new_list = ['one', 'two', 'three', 'four', 'five']

new_list.append('six') #puts six at the end of list
new_list[0] = 'ONE ALL CAPS' #appends to list

new_list.pop() #will take last element off list
new_list.pop()

popped_item = new_list.pop(0) #this will take off the element at position 0 and store it under popped_item

#you can't assign a variable to a sort method, so here's how you'll do it

new_list.sort() #can't attach a variable to this method. Reverse works the same
my_sorted_list = new_list #this will equal how you would want to do it

#dictionary
my_dict = {'key1':'value1', 'key2':'value2'}
my_dict['key1']

d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}

#another example

d = {'key1':['a', 'b', 'c']}

mylist = d['key1']