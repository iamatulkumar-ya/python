#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def get_neighbor(n, m, r, c, grid):
    neighbors = []
    if n-1 >=0:
        neighbors.append(grid[n-1][m])
        if m+1 <= c:
            neighbors.append(grid[n-1][m+1])
        if m-1 >=0:
            neighbors.append(grid[n-1][m-1])
            
    if n+1 <=r:
        neighbors.append(grid[n+1][m])
        if m+1 <= c: 
            neighbors.append(grid[n+1][m+1])
        if m-1 >= 0:
            neighbors.append(grid[n+1][m-1])
            
    if m+1 <= c:
        neighbors.append(grid[n][m+1])
    if m-1 >=0:
        neighbors.append(grid[n][m-1])
    
    return neighbors
    
def numCells(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
     
    dominentCell = []
    for i in range(n):
        for j in range(m):
            element = grid[i][j]
            max_neighors = max(get_neighbor(i, j, n-1, m-1, grid))
            if element > max_neighors:
                dominentCell.append(element)
    
    print(dominentCell)
    return len(dominentCell)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
