def fibonaci(limit):
  # the first two numbers are 0 and 1 and all the following numbers are a sum of the previous two numbers
  a, b = 0,1
  while a < limit: 
    yield a 
    a,b = b, a+b
    
fib = fibonaci(30)
for i in fib:
  print(i)
  
  