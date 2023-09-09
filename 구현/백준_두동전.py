import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def range_check(x, y):
    if not (0<=x<n and 0<=y<m):
        return True
    else: return False

def bfs():
    q=deque([(f_x, f_y, s_x, s_y, 0)])
    visited[f_x][f_y][s_x][s_y] = True
    
    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        
        if cnt >= 10:
            return -1

        for i in range(4):
            nx1, ny1, nx2, ny2 = x1+dx[i], y1+dy[i], x2+dx[i], y2+dy[i]
            if not range_check(nx1, ny1) and not range_check(nx2, ny2):
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                    
                if not visited[nx1][ny1][nx2][ny2]:
                    visited[nx1][ny1][nx2][ny2] = True
                    q.append((nx1, ny1, nx2, ny2, cnt+1))
            
            if range_check(nx1, ny1) and not range_check(nx2, ny2):
                return cnt+1
            elif range_check(nx2, ny2) and not range_check(nx1, ny1):
                return cnt+1
            else:
                continue
    return -1
            
if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    f_x, f_y, s_x, s_y = 0, 0, 0, 0
    flag = True
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                if flag:
                    f_x, f_y = i, j
                    flag = False
                else:
                    s_x, s_y = i, j
                    break
                
    print(bfs())