#to generate random number
import random

a = random.random
print(a)
# prints a random float from 0-1
#give it a range
b  = random.uniform(1,10)
#returns a random float between 1 and 10

#to make intergers
c = random.randint(1,10)
#this will include the upper border

d = random.randrange(1,10)
#wont include the upper border
print(a,b,c,d)

e = random.normalvariate(0,1)
# takes a mu (mean) and sigma(standard deviation), useful in statistics


#to take a random element in a list
mylist = list("abcdefgh")
f = random.choice(mylist)
print(f)
g = random.sample(mylist, 4)
#picks 4 unique elements from my list

h = random.choices(mylist, k = 3)
#list isn't necessarily unique as it can pick one number multiple times

i = random.shuffle(mylist)
#shuffles a list inplace

#these are all pseudo random generation as they can be reproduced with the seed function and not recomended to use in security sensitive situations

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))


random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))
