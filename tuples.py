#similar to a list, immutable, allows duplicate elements, iterabe 
#paranthesis are optional
mytuple = ("max", 28, "Boston")

'''to create a tuple from a list'''
my_list = [2,3,4,5,5,6,6]
my_tuple = tuple(my_list)
print(my_tuple)

my_tuple[0]

#tuple menthods
'''len(my_tuple)
my_tuple.count(5) tell you the number of 5 in the tuple
my_tuple.index(5) tell you the first occurance of 5
to convert to a list list(my_tuple)'''

#slicing
'''
ss
'''


a = (1,2,3,4,5,5) 
b = a[2:5]
#same as list

'''unpacking your tuple'''
my_tuple = "max", 28 , "Boston"
name, age, city = my_tuple
#similar to destuctring in js
# the number of elements in the variable side must match the number of elements in the tuple
#using * lets you put all the remaining elements into a list

i1, *i2  = my_tuple
print((i1,i2))

import sys
my_list = [0,4,5,6,6,4,55,6,6,6,7,7,7,7,6,5,4,4]
my_tuple = (0,4,5,6,6,4,55,6,6,6,7,7,7,7,6,5,4.4)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")