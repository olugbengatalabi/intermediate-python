#a decorator is a function that takes another function as an argument and extends the funtions of the function without explicitly modifying the function 

#two types, function decorator and class decorator
import functools

def mydecorator(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end") 
    return result
  return wrapper
    
    
@mydecorator
def print_name(yourname):
  print(yourname)
  
  

result = print_name("olugbenga")
print(result)
#if youre adding a decorator to a function that takes in an argument, the wrapper function in the decorator must take in thesame argument either by explit specification or by usig args and kwargs in the wrapper function


#add a decorator functools to the wrapper to tell python that its just a wrapper function helping it maintain a correct function identity
def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times = 4)
def greet(name):
  print(f"hello {name}")
  
greet("alex")


def debug(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    args_repr =[repr(a) for a in args]
    kwargs_repr = [f"({k} ={v!r}" for k,v in kwargs.items()]
    signature = ",".join(args_repr + kwargs_repr)
    print(f"calling {func.__name__}({signature})")
    result = func(*args, **kwargs)
    print(f"{func.__name__!r} returned {result!r}")
    return result
  return wrapper




#you can stack decorators up
@debug
@mydecorator
def say_hello(name):
  greeting = f"hello {name}"
  print(greeting)
  return greeting

say_hello("aller")

#class decorator

class CountCalls:
  def __init__(self, func):
      self.func = func
      self.num_calls = 0
  
  def __call__(self, *args, **kwargs):
      self.num_calls += 1
      print(f"this has been executed {self.num_calls} times")
      return self.func(*args, **kwargs)
    
@CountCalls
def say_hello():
  print("hello")
  
say_hello()