
# collections : Counter, namedtuple, orderedDic, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict,defaultdict,deque
#a counter is  contineer that stores element as dictionary keys and their count as dictionary values
a = "aannnnnnnnnnppppppppfff"
my_counter = Counter(a) 
print(my_counter)
print(my_counter.values())
print(my_counter.keys())
print(my_counter.most_common(1))
print(my_counter.most_common(2))
# to get the key to the most commot element
print(my_counter.most_common(1)[0][0])
#if you want it to create a list appending it with each item as it counts the element, 
print(list(my_counter.elements()))


#NAMAEDTUPLES
# IT IS AN EASY TO CRETE AND LIGHTWEIGHT OBJECT TYPE
Point = namedtuple("Point", "x,y")
#the first argument is the class name,the second argument is the different field you want to create
#this will create a class named point with the fields x and y 
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)


#ordered dictionary
#its a dictionary that remembers the order of the elements in it
#less important now because newer python version can remeber the order of their elements

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)

dicx = {"a":1,"b":2,"c":3,}
dicx["d"] = 4
print(dicx)


#default dict
#similar to a normal dictionary, but will have a defualt value if the key is not set yet

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d["d"])
#returns 0

e = defaultdict(list)
e["a"] = 1
e["b"] = 2
e["c"] = 3
print(e["e"])
#returns []

f = defaultdict(float)
f["a"] = 1
f["b"] = 2
f["c"] = 3
print(f["f"])
#returns []

#if this was a normal dictionary, this will raise a key error 



#deque is a double ended queue, can be used to remove or add elements from both ends

d = deque()
d.append(1)
d.append(2)
d.append(3)

d.appendleft(4)
d.append(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear() #removes all element

#to add multiple elements at a time
d.extend([2,3,4,5,])
print(d)
d.extendleft([0,2,3,4])
print(d)

#you can rotate the deck
d.rotate(1) # rotate all elements one place to the right
d.rotate(-1) # rotate all elements one place to the left