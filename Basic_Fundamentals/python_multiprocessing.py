## or CPU-bound tasks (e.g., heavy computations), 
# Python's GIL prevents threads from achieving true parallelism. 
# In such cases, multiprocessing is often a more suitable alternative, as it creates separate processes, each with its own interpreter and memory space, allowing for parallel execution on multiple cores.


