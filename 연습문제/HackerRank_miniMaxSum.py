#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min=0
    max=0
    
    arr.sort()
    
    for idx, num in enumerate(arr):
        if idx==0:
            min+=num
        elif idx==4:
            max+=num
        else:
            min+=num
            max+=num
            
    print(min, max)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
