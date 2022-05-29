from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_square(x,y):
    
    for wall_x, wall_y in walls:
        if x <=wall_x<x+h and y <= wall_y<y+w:
            return False
    return True

def count_walls():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                walls.append([i,j])
    
if __name__ == "__main__":
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    h, w, s_r, s_c, f_r, f_c = map(int, input().split())
    visited = [[False for _ in range(m)] for _ in range(n)]
    walls = []
    
    q = deque()
    count_walls()
    
    q.append([s_r-1, s_c-1, 0])
    
    while q:
        x, y, cost = q.popleft()
        visited[x][y] = True
        
        if x+1 == f_r and y+1 == f_c:
            print(cost)
            exit(0)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and 0<= nx+h-1<n and 0<=ny+w-1<m:
                if not visited[nx][ny]:
                    if check_square(nx,ny):
                        visited[nx][ny] = True
                        q.append([nx, ny, cost+1])
                        
    print(-1)