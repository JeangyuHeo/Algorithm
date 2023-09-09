import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    global visited
    
    q = deque()
    
    q.append((x,y))
    visited[x][y] = True

    cnt = 0
    flag = True
    while q:
        cur_x, cur_y = q.popleft()
    
        for i in range(4):
            nx, ny = cur_x+dr[i], cur_y+dc[i]
            
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if board[nx][ny] == 0:
                        flag = False
                    elif board[nx][ny] == 2:
                        visited[nx][ny] = True
                        cnt+=1

                        q.append((nx, ny))
    if flag:
        return cnt + 1
    else:
        return 0
    
if __name__ == "__main__":
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)
    
    answer = 0
    
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    empty_list = []
    
    for r in range(n):
        for c in range(m):
            if board[r][c] == 2:
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0<=nr<n and 0<=nc<m:
                        if board[nr][nc] == 0:
                            empty_list.append((nr, nc))
    
    len_empty = len(empty_list)
    
    for i in range(len_empty-1):
        for j in range(i+1, len_empty):
            visited = [[False for _ in range(m)] for _ in range(n)]
            r1, c1 = empty_list[i][0], empty_list[i][1]
            r2, c2 = empty_list[j][0], empty_list[j][1]
            
            board[r1][c1] = 1
            board[r2][c2] = 1
            
            for r in range(n):
                for c in range(m):
                    if board[r][c] == 2:
                        if not visited[r][c]:
                            visited[r][c] = True
                            answer = max(bfs(r,c), answer)

            board[r1][c1] = 0
            board[r2][c2] = 0
            
    print(answer)