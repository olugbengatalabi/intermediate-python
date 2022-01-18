# one line annonymous function
from audioop import add


add10 = lambda x : x + 10

print(add10(5))

mult = lambda x,y : x * y

print(mult(2,7))

#used when  function is to be called just once or when it is to be passed into higher order function

points2D = [(1,2), (15,2), (5, -1), (10, 4)]


points2D_sorted2 = sorted(points2D)
#by default, it sorts it by the first argument. a lamda function can be passed in to tell it sort by the second arguments instead

points2D_sorted = sorted(points2D, key=lambda x:x[1])
print(points2D_sorted)

#to sort according the sum
points2D_sortedsum = sorted(points2D,key =  lambda x: x[0] + x[1])
print(points2D_sortedsum)

## the map funtions
##map(func, seq)
lista =[ 1,2,3,4,5]
listb = map(lambda x : x*2, lista)
print(list(listb))

#or use list comprehension

listc = [x*2 for x in lista]
print(listc)

#filter(func, squ)
listd = filter(lambda x:x%2 ==0, lista)
#or list comprehension
liste = [x for x in lista if x%2==0]
print(list(listd), liste)


from functools import reduce
##reduce function
#refuce (func, seq)
product_A = reduce(lambda x,y: x*y, lista)
print(product_A)
