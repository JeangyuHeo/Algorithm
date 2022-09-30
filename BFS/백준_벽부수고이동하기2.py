from collections import deque

if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    
    n, m, k = map(int, input().split())
    board = [input() for _ in range(n)]
    
    visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    
    q = deque([(0,0,0,1)])
    visited[0][0][0] = True
    
    while q:
        cur_x, cur_y, cnt, res = q.popleft()
        if (cur_x, cur_y) == (n-1, m-1):
            print(res)
            exit()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            
            
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == '1':
                    if cnt < k:
                        if not visited[nx][ny][cnt+1]:
                            visited[nx][ny][cnt+1] = True
                            q.append((nx, ny, cnt+1, res+1))
                else:
                    if not visited[nx][ny][cnt]:
                        visited[nx][ny][cnt] = True
                        q.append((nx, ny, cnt, res+1))
    
    print(-1)