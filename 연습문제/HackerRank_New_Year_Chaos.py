#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    q = [i-1 for i in q]
    bribes = 0
    
    for idx, pos in enumerate(q):
        cur = idx
        if pos - cur > 2:
            print("Too chaotic")
            return
        for k in q[max(pos - 1, 0): idx]:
            if k > pos:
                bribes += 1
    print(bribes)
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
