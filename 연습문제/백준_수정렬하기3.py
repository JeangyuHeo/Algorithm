import sys

num = int(sys.stdin.readline())
count_sort = [0] * 10001

for _ in range(num):
    item = int(sys.stdin.readline())
    count_sort[item] += 1
    
for i in range(10001):
    if count_sort[i] != 0:
        for _ in range(count_sort[i]):
            print(i)