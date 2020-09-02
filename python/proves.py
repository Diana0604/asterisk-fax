import multiprocessing 
import time 
  
def func(number): 
    for i in range(1, 10): 
        time.sleep(0.01) 
        print('Processing ' + str(number) + ': prints ' + str(number*i)) 
  
# list of all processes, so that they can be killed afterwards  
all_processes = [] 
  
for i in range(0, 3): 
    process = multiprocessing.Process(target=func, args=(i,)) 
    process.start() 
    all_processes.append(process) 
  
# kill all processes after 0.03s  
time.sleep(0.03) 
for process in all_processes: 
    process.terminate() 