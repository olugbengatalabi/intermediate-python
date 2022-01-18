# ###differente between syntax erro and exception
# #type error, import error, name error, file not found error, 
# # value error: if an operation recieve an argument that has the right type but an inappropiate value, index error

# x = -5
# if x < 0:
#   raise Exception("x should be positive")
# ##or
# assert (x>= 0), "x is not positive"

# try:
#   a = 5 / 0
# except Exception as e:
#   print("an error happened " + e)
  
  

# try:
#   a = 5 / 0 
#   b = a+4
# except ZeroDivisionError as e:
#   print("an error happened " +e )
# except TypeError as e :
#   print(e)
# else:
#   print("there was not exception called")
  
# finally:
#   print("this runs always whether or not there is an exception or not")
  
  
  
##to define your own exception 
class ValueTooHighError(Exception):
  pass

class ValueTooSmallError(Exception):
  def __init__(self, message,value):
    self.message = message
    self.value = value

def test_value(x):
  if x>100:
    raise ValueTooHighError("value is too high")
  elif x<50 :
    raise ValueTooSmallError("value is too small", x)
  
# test_value(200)

try:
  test_value(2000)
except ValueTooHighError as v:
  print(e)
except ValueTooSmallError as e:
  print(e.message, e.value)