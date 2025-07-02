
import time
import random

def max_profit(inventory, order):
    st = time.time()
    maxProfit = 0
    while order !=0:
        inventory = sorted(inventory, reverse=True)
        maxProfit += inventory[0]
        inventory[0] = inventory[0] - 1
        order -=1

    print(f"total execution time: {time.time() - st} ") 
    return maxProfit
    
if __name__ == '__main__':
    inventory = [random.randint(1,15) for _ in range(1, 100000)]
    order = 5000
    print(max_profit(inventory, order))