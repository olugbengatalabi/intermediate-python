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