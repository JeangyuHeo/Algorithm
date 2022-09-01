import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque([1])
    visited[1] = True
    
    while q:
        cur = q.popleft()
        
        for i in range(1, 7):
            next = cur+i
            if 0<next<101 and not visited[next]:
                if next in ladders.keys():
                    next = ladders[next]
                    
                if next in snakes.keys():
                    next = snakes[next]
                    
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    dp[next] = dp[cur] + 1
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [False for _ in range(101)]
    dp = [0 for _ in range(101)]
    
    ladders, snakes ={}, {}
    
    for _ in range(n):
        from_, to_ = map(int, input().split())
        ladders[from_] = to_
        
    for _ in range(m):
        from_, to_ = map(int, input().split())
        snakes[from_] = to_
        
    bfs()
    
    print(dp[100])