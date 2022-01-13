# oredered, mutable and allows duplicate elements
# len(mylist), 
# mylist.insert(1, "bluberry")
#mylist.pop() returns the last item and removes it
'''
mylist.remove(item)
mylist.clear(removes all elements)
mylist.revers()
mylist.sort()'''

my_list = [1,2,3,4,5,6,-2,-4,-5]
print(my_list.sort())
# sort() returns none, sorts the list in place, i.e changes the original list
print(my_list)

new_list = sorted(my_list)
# sorted doesnt change the original list but returns a new list containing the same elements but in ascending order

# to create a new list with same elements in multiple
mlist2 = [2] * 10
print(mlist2)

''' you can concatenate lists using newlist = listname1 + listname2'''


#list slicing
a = my_list[0:5]
#specifiy the start and stop index
print(a)

b = my_list[:4]
print(b)
#to add a step index, the last one here defines the step
c = my_list[1:6:2]
d = my_list[1::2]
print(c,d)
#you can also specify a negative index
e = my_list[::-1]


'''to copy your list
if you just use list1 = list2, the two list become tied together and mutating list1 will cause mutation in list2. instead do.'''
list_copy = my_list.copy()
#or
list_copy2 = list(my_list)
#or use slice
list_copy = my_list[:]


#to square all the numbers in a list, and create a new list out of it
#or use list comprehension 
my_numbers = [1,2,3,4,5,6]
my_new_list = [i*i for i in my_numbers]
print(my_new_list)