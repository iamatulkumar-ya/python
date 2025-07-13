
import heapq
import random
import time
def max_profit(inventory, order):
    st = time.time()
    # Convert inventory to a min-heap.
    # To get the largest elements efficiently, we store their negatives.
    # So, the smallest element in the heap will be the largest absolute value.
    max_heap = [-item for item in inventory]
    heapq.heapify(max_heap)

    total_profit = 0

    while order > 0 and max_heap:
        # Get the largest available inventory item (which is the smallest negative in the heap)
        current_max_value = -heapq.heappop(max_heap)

        # If the current max value is 0, we can't sell any more for profit
        if current_max_value == 0:
            break

        total_profit += current_max_value
        
        # Decrease the value and push it back to the heap
        heapq.heappush(max_heap, -(current_max_value - 1))
        
        order -= 1

    print(f"total execution time: {time.time() - st}")
    return total_profit

if __name__ == '__main__':
    inventory = [random.randint(1,15) for _ in range(1, 100000)]
    order = 5000
    print(f"max profit  :{max_profit(inventory, order)}") # Expected: 18 (5+4+3+6)
 