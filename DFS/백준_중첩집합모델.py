import sys
from collections import defaultdict

def check_leaf(idx):
    result = True
    check_list = connect[idx]
    
    for node in check_list:
        if not visited[node]:
            result = False
    return result
    
def dfs(idx, start_range):
    
    if check_leaf(idx):
        range_info[idx]=[start_range, start_range+1]
        return start_range + 2
    
    next_range = start_range+1
    
    for next in connect[idx]:
        if not visited[next]:
            visited[next] = True
            next_range = dfs(next, next_range)
            range_info[idx] = [start_range, next_range]
    
    return next_range+1

    
if __name__ == "__main__":
    sys.setrecursionlimit(1000000000)
    n = int(input())
    connect = defaultdict(set)
    visited = [False for _ in range(n+1)]
    range_info = {}
    root = -1
    
    while True:
        connections = list(map(int, input().split()))
        if connections[-1] != -1:

            root = connections[0]
            break
        start = connections[0]
        for j in connections[1:]:
            if j != -1:
                connect[start].add(j)
                connect[j].add(start)

    for key, val in connect.items():
        connect[key] = sorted(val)
    
    visited[root] = True
    max_range = dfs(root, 1)
    
    for num, (start, end) in sorted(range_info.items(), key=lambda x: x[0]):
        print(num, start, end)


    """
test example)

input)

17
1 2 3 -1
2 4 5 -1
3 6 7 8 -1
4 9 10 -1
5 11 -1
6 12 13 -1
7 14 15 16 -1
8 17 -1
1

output)

1 1 34
2 2 13
3 14 33
4 3 8
5 9 12
6 15 20
7 21 28
8 29 32
9 4 5
10 6 7
11 10 11
12 16 17
13 18 19
14 22 23
15 24 25
16 26 27
17 30 31

    """