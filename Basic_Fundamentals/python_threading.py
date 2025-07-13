# The threading module provides a way to run multiple threads (smaller units of a process) concurrently within a single process.
# with sharing memory space. 



import threading
import time
from datetime import datetime

global results
results = []


def do_process(process_name:str, delay:int):
    
    print(f"Execution started for process: {process_name} on {datetime.now()}")
    time.sleep(delay)
    print(f"\nExecution ended for process: {process_name} on {datetime.now()}")
 

def do_process1(process_name:str, delay:int):
    
    print(f"Execution started for process 1: {process_name} on {datetime.now()}")
    time.sleep(delay)
    results.append(f"Completed process - {process_name}")
    print("results value in thread method", results)
    print(f"\nExecution ended for process 1: {process_name} on {datetime.now()}")
    
 

process= [
    "process1",
    "process2",
    "process3"
]

threads = []
for p in process:
    # creating thread for each process
    delay = 3
    if p == "process2":
        delay = 6

    # The target is the function to be executed by the thread whereas the args is the arguments to be passed to the target function. 

    if p == "process1":
        t = threading.Thread(target=do_process1, args=(p, delay))
    else:
        t = threading.Thread(target=do_process, args=(p, delay))
    
    threads.append(t)

    if p == "process2":
        t.daemon = True 


if __name__ == '__main__':
    print("main started", datetime.now())
    # let's start the threads
    for t in threads:
        t.start()
        print("thread id", t.native_id)
    print("\n All threads have been started")


    # let's wait for each threads to finish
    for t in threads:
        t.join()

    print("\n All threads have been joined")

    # this value will be same as process assignment value because, in threading memory utilization gets shared for all threads
    print("results value in main", results) 
    print("main completed", datetime.now())




