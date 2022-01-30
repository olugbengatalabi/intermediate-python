import json
from textwrap import indent

# javascript object notation

#serialization or encoding: the process of converting to a json format

person = {
    "name": "john",
    "age":30,
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(person,indent= 4, sort_keys=True )
print(personJSON)
with open("person.json", "w") as file:
    json.dump(person, file, indent= 4)
#to dumpinto a file

#whats the difference between dump and dumps


#to conver json data back to a dictionary i.e deserialization or decoding 

person = json.loads(personJSON)
print(person)

#to create it from a file
with open("person.json", "r") as file:
    person2 = json.load(file)
    print(person2)
