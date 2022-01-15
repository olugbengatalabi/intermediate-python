#set : collection dta type thats unordered and mutable
#similar to a dict, but doesnt take key,value pairs just singles
# sets do not allow duplicates


#creating a set

myset = set([1,2,3,])
myset2 = set("hello")
print(myset, myset2)

#notice the arbituary order and how only one hello is printed

#to create an empty set
myset3 = {}
#? this will create a dictionary not a set, instead do
myset4 = set()

myset4.add(4)
myset.add(5)
myset4.remove(4)

#if you dont know if an element is in a set but want to remove if its there use discard to avoid raising an error
myset.discard(8)

myset.clear()
myset2.pop()
#since a set has an arbituary ordering, any of the elements can get pop
print(myset2)

#can be looped over with a forloop 


#? UNION AND INTESECTIONS IN A SET
odds = {1,3,5,7,9}
even = {2,4,6,8,0}
prime = {2,3,5,7,11}

union1 = odds.union(even)
#returns the combination of elements of the two sets without duplication
print(union1)

intersection = odds.intersection(prime)
#returns the elements that are present in the two sets

setA = {1,2,3,4,5,6,7}
setB = {5,6,7,8,9,10}

# diff = setA.difference(setB)
# print(diff)
# #this returns the elements in set a that are not in setB ie. 1234

# diff2 = setB.difference(setA)
# print(diff2)

# diff3 = setA.symmetric_difference(setB)
#returns a set with all the element that are in set a or b but not in both

#to modify a set inplace use update

# setA.update(setB)
#this add all the elements that are in set b to setA without duplication

setA.intersection_update(setB)
print(setA)
#this updates the set by keeping only the elements found in both 


setB.difference_update(setA)
# this updates the set by removing the elements not found in another sent

#symmetric differnce update keeps the element that are in set a  or b but not in both

setC = {1,2,3,4,5,6,7,8}
setD = {5,6,7,8} 
#superset and subset, disjoint method
print(setD.issubset(setC))
print(setC.issuperset(setD))
print(setC.isdisjoint(setD))
#returns false becuse they have elements that are found in both sets


#copying a set
setE = set(setC)
#or
setF = setC.copy()

#frozensetj