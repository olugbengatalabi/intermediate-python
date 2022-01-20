import logging
import traceback
try:
  a = [1,2,3,4,5]
  val = a[5]
except IndexError as e:
  print(e)
  
  
try:
  a = [1,2,3,4,5]
  val = a[5]
except IndexError as e:
  logging.error(e)
  
#to see a traceback
try:
  a = [1,2,3,4,5]
  val = a[5]
except IndexError as e:
  logging.error(e, exc_info=True)
  
#if you dont know which type of error to catch, iport the traceback moduele
try:
  a = [1,2,3,4,5]
  val = a[5]
except:
  logging.error("the error is %s", traceback.format_exc())