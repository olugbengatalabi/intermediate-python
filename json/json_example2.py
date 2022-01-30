import json 

class User:
  
  
  def __init__(self, name, age) -> None:
      self.name = name
      self.age = age
    
user = User("mike", 5)

#to encode this into json 
#method 1
def encode_user(o):
  if isinstance(o, User):
    return {"name": o.name, "age": o.age, o.__class__.__name__ : True}
  else:
     raise TypeError("object of type user is not JSON serializable")
   
   
   
   #either
userJSON = json.dumps(user, default= encode_user)

#method2
#here a new class is create that inherits from the inbuilt json encoder. overwrite the default class and configure to load up your desired class
from json import JSONEncoder
class UserEncoder(JSONEncoder):
  def default(self, o):
    if isinstance(o, User):
      return {"name": o.name, "age": o.age, o.__class__.__name__ : True}
    return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls = UserEncoder )


#method 3

userJSON = UserEncoder().encode(user)

print(userJSON)

#to decode the objects back to a dictionary

user = json.loads(userJSON)
print(user)

#to decode it back to a user object you have to write a custom decoding method

def decode_user(dict):
  if User.__name__ in dict:
    return User(name = dict["name"], age = dict["age"])
  return dict

user = json.loads(userJSON, object_hook= decode_user)
print(user.name)