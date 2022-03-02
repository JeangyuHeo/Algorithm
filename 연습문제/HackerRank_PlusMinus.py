#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    plus=0
    minus=0
    zero=0
    
    for num in arr:
        if num >0:
            plus+=1
        elif num < 0:
            minus+=1
        else:
            zero+=1
    print(f"{plus/total:.6f}\n{minus/total:.6f}\n{zero/total:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)