from threading import  Thread, Lock
import time 

# def square_numbers():
#   for i in range(100):
#     i*i
    
# threads = []
# num_threads = 10

# #to create the process  
# for i in range(num_threads ):
#   t = Thread(target = square_numbers)
#   threads.append(t)
  
# #start
# for p in threads:
#   p.start()
  
# #join
# for p in threads:
#   p.join()
  
  
#sharing data between threads
database_value = 0


def increase():
  global database_value
  # with lock:
  local_copy = database_value
  local_copy += 1  
  #with time.sleep the prodram is put on hold and the other thread runs, it changes the value of database value to 1 from zore and thread one does that too. so the database value still 1 not 2
  time.sleep(0.1)
  database_value = local_copy




if __name__ == "__main__":
  print("start value", database_value)
  
  thread1 = Thread(target=increase())
  thread2 = Thread(target=increase())
  
  print("end value", database_value)
  #your end value is printing 2, should be one since there is a race condition i.e two or more threads are trying to modify thesame value in a process
  
  #if end value is one, then use a lock object to aquire and release, while auired, it prevents the system from switching to the second thread even tho there is a time.sleep