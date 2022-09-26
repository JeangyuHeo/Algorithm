import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    dr = (-2, -2, 0, 0, 2, 2)
    dc = (-1, +1, -2, 2, -1, 1)

    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    q = deque([(r1, c1, 0)])
    visited[r1][c1] = True
    
    while q:
        r, c, cnt = q.popleft()

        if (r,c) == (r2,c2):
            print(cnt)
            quit()
        
        for i in range(6):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<n:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt+1))
                    
    print(-1)