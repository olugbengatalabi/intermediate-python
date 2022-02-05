from multiprocessing import Process
import os

def square_numbers():
  for i in range(100):
    i*i
    
processes = []
num_processes = os.cpu_count()

#to create the process  
for i in range(num_processes):
  p = Process(target = square_numbers)
  processes.append(p)
  
#start
for p in processes:
  p.start()
  
#join
for p in processes:
  p.join()