import secrets
#for passwords and security tokes
#has only 3 function

a = secrets.randbelow(10)
#produce a random integer from o- 10 and 10 isnt  included

b = secrets.randbits(4)
#this will return an integer will 4 bits (in binary, e.g 1101)

my_list = list("abcdfgh")
c = secrets.choice(my_list)