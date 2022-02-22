#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    row = len(arr)
    col = len(arr[0])
    
    left_start=0
    right_start=0
    
    for idx in range(row):
        left_start += arr[idx][idx%col]

    cnt=0
    for idx in range(row-1, -1, -1):
        right_start += arr[idx][cnt%col]
        cnt+=1
            
    return abs(left_start - right_start)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
