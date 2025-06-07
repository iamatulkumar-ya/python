## or CPU-bound tasks (e.g., heavy computations), 
# Python's GIL prevents threads from achieving true parallelism. 
# In such cases, multiprocessing is often a more suitable alternative, as it creates separate processes, each with its own interpreter and memory space, allowing for parallel execution on multiple cores.


# importing the multiprocessing module
import multiprocessing
from datetime import datetime
import time

global cubeResult
cubeResult = 0


def print_cube(num): 
    
    time.sleep(2)
    cubeResult = num * num * num
    print("Cube: {}, computed on {}".format(cubeResult, datetime.now()))
  

def print_square(num): 
    print("Square: {}, computed on {}".format(num * num, datetime.now()))

if __name__ == "__main__":
    print("main process started on ", datetime.now())
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    print("p1 process id", p1.pid)
    print("p2 process id", p2.pid)

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # printing cubeResult
     # this value will be empty as, in multiprocessing memory utilization is different for each process
    print("cubeResult in main", cubeResult) # will give 0 as multiprocesing runs in different memory space

    # both processes finished 
    print("main process completed on ", datetime.now())