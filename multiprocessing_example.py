from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_100(number, lock):
  for i in range(100):
    time.sleep(0.01)
    #locks the code below preventing any other process from interacting with it will it modefies it
    with lock:
      number.value += 1
    #releases it to be accessed by other processes
    
    
    
if __name__ == "__main__":
  lock = Lock()
  shared_number = Value("i", 0)
  print("number at the beging is ", shared_number.value)
  p1 = Process(target = add_100, args = (shared_number,lock))
  p2 = Process(target = add_100, args = (shared_number,lock))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  print("number at the end is", shared_number.value)
  
  
  #two processes are trying to modify the value of the shared variable at thesame time, this is called a race condition and it can lead to incorrect results
  #to prevent this you must use a lock, which prevents another process from accessing the shared variable when it is already being worked on
  
 
 
def add_102(numbers, lock):
  for i in range(100):
    time.sleep(0.01)
    for i in range(len(numbers)):
      with lock:
        numbers[i] += 1
    
    
     


if __name__ == "__main__":
  lock = Lock()
  shared_array = Array("d", [-0.0, 100.0, 200.0])
  print("array at the beging is ", shared_number.value)
  a1 = Process(target = add_102, args = (shared_array,lock))
  a2 = Process(target = add_102, args = (shared_array,lock))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  print("number at the end is", shared_number.value)
  
  