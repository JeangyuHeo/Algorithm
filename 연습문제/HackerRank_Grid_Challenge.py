#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for idx, s in enumerate(grid):
        s = sorted(s)
        grid[idx] = s
        for idx in range(len(s)-1):
            if s[idx] > s[idx+1]:
                return 'NO'
    
    length = len(grid[0])
    
    for i in range(length):
        for j in range(length-1):
            if grid[j][i] > grid[j+1][i]:
                return 'NO'
        
    return 'YES'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
