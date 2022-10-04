import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def dfs(num, total):
    global res,visited, end_point
    
    if visited[num]:
        return 
    if total > res:
        res = total
        end_point = num
        
    visited[num] = True
    
    for cost, next in graph[num]:
        dfs(next, total+cost)
        
    visited[num] = False
    
if __name__ == "__main__":
    n = int(input())
    graph = defaultdict(list)
    
    for _ in range(n-1):
        parent, child, cost = map(int, input().strip().split())
        
        graph[parent].append((cost, child))
        graph[child].append((cost, parent))
    
    res = 0
    end_point = 0
    visited = [False for _ in range(n+1)]
    
    dfs(1, 0)
    
    dfs(end_point, 0)

    print(res)