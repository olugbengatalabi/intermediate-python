my_dict = {"name": "max", "age":25, "city":"new york"}
print(my_dict)

value = my_dict["name"]
print(value)



#to mutate
my_dict["email"] =  "maz@xyz.com"
#if the key already exists, it just overwrites the og item


#to delete
del my_dict["name"]
print(my_dict)
#or
my_dict.pop("age")
#or
my_dict.popitem()
#removes the last inserted item

#to check if an item in dict
if "name" in my_dict:
  print(my_dict["name"])
  
#or
try:
  print(my_dict["name"])
except:
  print("error")
  
  

for key in my_dict:
  print(key)

#or
for key in my_dict.keys():
  print(key)

for value in my_dict.values():
  print(value)
#looops through the dict and return the keys

for key, value in my_dict.items():
  print(my_dict)
  
  
#to copy the dictionary
my_dict_copy = my_dict

#in this method, any edit to my_dict_copy will also mutuate my_dict

#a more ccurate copy 
my_dict_copy2 = dict[my_dict]



#to update a dictionary
my_dict1 = {"name": "max", "age":29, "email":"olug@veo.xz"}
my_dict2 = dict(name = "mary", age= "27", city = "boston")

my_dict1.update(my_dict2)
print(my_dict1)
#this goes through the new dict and find any key thts not in the dictionary to be updated and it add it to it, for the keys that are already present in dict1, the values are overwriten

