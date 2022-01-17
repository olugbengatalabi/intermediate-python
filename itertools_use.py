from itertools import product, permutations, combinations, combinations_with_replacement,accumulate, groupby,count,cycle,repeat
import operator

# a = [1,2] 
# b = [3,4]
# prod = product(a,b)
# print(prod)
# print(list(prod))


# prod2 = product(a,b, repeat = 2)
# print(list(prod2))
# #permutations return all possible orderings of an input

# p = [1,2,3]
# perm = permutations(p)
# print(list(perm))

# #you can specifity the length of the permutation
# perm2 = permutations(p, 2)
# print(list(perm2))

#combinations
com = [1,2,4,5]
combin = combinations(com, 1)
# the second argument with the length is mandatory
print(list(combin))

#no that there are no combination reoitition
#import combinations with replacements

cobin_with_r = combinations_with_replacement(com,2)
print(list(cobin_with_r))

acc_list = [1,2,3,4]
acc = accumulate(acc_list)
print(acc_list)
print(list(acc)) 

acc2 = accumulate(acc_list, func = operator.mul)
#multiplies the element
print(list(acc2))

acc3 = accumulate(acc_list, func = max)
#multiplies the element
print(list(acc3))



#group by makes an iterator that return keys in groups from an iterable
def smaller_thant_3(x):
  return x < 3
group_obj = groupby(acc_list, key = smaller_thant_3 )
for key,value in group_obj:
  print(key,list( value))
  
  
#lambas are small one line function that can recieve inputss and return values
group_obj2 = groupby(acc_list, key = lambda x : x < 3 )
for key,value in group_obj2:
  print(key,list( value))
  
  
###example 2
persons = [
  {"name": "Tim", "age": 25},
  {"name": "Dan", "age": 25},
  {"name": "Claire", "age": 27},
]

group_obj3 = groupby(persons, key = lambda x : x ['age'] )
for key,value in group_obj3:
  print(key,list( value))
  
  
  
for i in count(10): 
  print(i)
  if i == 15:
    break
# if the break statement isnt added, it will count from 10 to infinity

listry = [1,2,3] 
for i in cycle(listry): 
  print(i)
  if i == 15:
    break
  
  #cycle through
  
for i in repeat(1,4):
  #repeat 1 4 times, if not included, it will repeat till infinity
  print(i)