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

letter = mylist[2] #to reassign what the list is item is

#to add to a dictionary
d = {'k1': 100, 'k2':200}
d['k3'] = 300 #this will add k3 to the dictionary

#to change a key value
d = ['k1'] = 'NEW VALUE'

#to return all the keys
d.keys() #will return dict_keys(['k1', 'k2', 'k3'])

#return values
d.values()

#to return dictionary
d.items() #you'll get: dict_items(['k1',100), ('k2', 200), ('k3', 300)])

#tuples us () while lists use []
#they're immutable

mylist[0] = 'NEW' #reassigns NEW to the list at index 0 when called
t[0] = 'NEW' #will give you an error message because you can't reassign items in tuples

#people use tuples for data integrity. When passing around objects in programs, you need to make sure that they don't
#  change. 