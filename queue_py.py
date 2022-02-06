from threading import Thread, Lock, current_thread
from queue import Queue
import time


# a queue is a linear data structure that follows the first in first out principle.. first come fist serve


# if __name__ == "__main__":
#    q = Queue()
#    q.put(1)
#    q.put(2)
#    q.put(3)
#    #321 -->
#    first = q.get()
#    print(first)
#    q.task_done() # used in multithreading environments to tell that the task is done and another thread can be worked on
#    q.empty()
#    q.join #blocks the main thread while this thread is being executed
#    print("end main")
   
   
def worker(q):
  while True:
    value = q.get()
    #since q is empty but lock, the function will wait until we fill q(k) with element
    #processing
    with lock:
      print(f"in {current_thread().name} got {value}")
    q.task_done()

if __name__ == "__main__":
  k = Queue()
  lock = Lock
  num_threads = 10
  
  for i in range(num_threads):
    thread = Thread(target = worker, args = (k,lock   ))
    thread.daemon = True
    #a background thread that dies when the main thraed dies 
    thread.start() 
  
  for i in range(1, 21):
    k.put(i)
    
  k.join()
  #blocks the main thread
  
  print("end main")