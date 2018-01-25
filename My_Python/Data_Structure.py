# Introduction to Data Structures

# Lists
'''
List is mutable

'''
example_list_1 = ['A', 'B', 'C', 'D']

example_list_2 = [x for x in range(10)]

example_list_3 = [(x,y) for x in range(10) for y in range(10,20) if x != y]

# Tuples
'''
Tuple is immutable

'''

example_tuple_1 = 12, 323, 'Hello'

example_tuple_2 = (12, 323, 'Hello')

# Sets
'''
Set has no duplicate elements

'''

example_set_1 = {'Hello', 'World', '!'}

example_set_2 = { x for x in 'asdfsdfgdsf' if x not in 'agf'}

# Dictionaries
'''
Dictionary is an unordered set of key:value pairs

'''
a = [1,2,3,4,5]
b = ['A','B', 'C', 'D', 'E']

example_dict_1 = dict([(a[x],b[x]) for x in range(len(a))])

example_dict_2 = {'jack':4098, 'space':23, 'object': 121, 'house':10}

example_dict_3 = dict(sape=4139, guido=4127, jack=4098)

example_dict_4 = {x: x**2 for x in (2, 4, 6)}




