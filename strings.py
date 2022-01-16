my_stg = "hello shit"
characterooo = my_stg[2]
#even though you can access a character, you can't change the vlues

#slicing
nstring = my_stg[1:4]
substring = my_stg[1:10:3]
print(substring)


greeting = "      hello   maen "
name = "Tom"
sentence = greeting + " " + name


#to remove whitespace, use strip()
print(greeting.strip())
#since a string is immutable, it doesnt  change the string inplace, s
print(greeting)

#to uppercase use
greeting.upper()
greeting.lower()

#to check what it starts with
print(greeting.startswith("hello"))
print(greeting.endswith("maen "))

#to find
print(greeting.find("o"))
#to count 
print(greeting.count("l"))

#replace
print(greeting.replace("hello", "hi"))
# ? doesnt change the og string,
# ? if it doesnt find the word to be replces, it does nothing

stringy1 = "how are you doing"
mylist = list(stringy1)
print(mylist)
mylist2 = stringy1.split()
print(mylist2)
mylist3 = stringy1.split("a")

#to convert the list back to a string

mylist4 = " ".join(mylist2)
# concatenates all of our elements in the list, with the seprator being what is passwed between the " "
print(mylist4) 

#HOW TO KNOW THE TIME IT TOOK TO EXECUTE A CODE
from timeit import default_timer as timer
start = timer()
mylist4 = " ".join(mylist2)
stop = timer()
print(stop-start)


#string formating with f stringss
#1 using %
var = 3.123
var2 = 5.555
my_string = "the variable is %f" %var
print(my_string)
my_string2 = "the variable is %.2f" %var
#print in 2 decimal places
print(my_string2)

#2 using the .format method
my_string3 = "the variables are {:.2f} and {}".format(var, var2)
print(my_string3)

#3 with the f string
my_string4 = f"the variable is {var} and {var2 * 2}"
#print in 2 decimal places
print(my_string4)
