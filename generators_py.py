import sys
def mygenerator():
  yield 1
  yield 2
  yield 3
  
g = mygenerator()
print(g)

for i in g:
  print(i)
  
value = next(g)
print(value)
  
value = next(g)
print(value)
  
value = next(g)
print(value)
  
value = next(g)
print(value)


you can also use it to pass arguments into functions that take iterables 

print(sum(g))
print(sorted(g)) 


def countdown(num):
  print("starting")
  while num > 0:
    yield num
    num -= 1
  
cd = countdown(4)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))

#generators are very memory efficient 
def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums

# a more memory efficient way to do this is to use generators
def firstn_generators(n):
  num = 0
  while num < n:
    yield num
    num += 1
    
    
print(firstn(10))
j = firstn_generators(10)
print(next(j))

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generators(100000)))



