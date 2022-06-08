from collections import deque

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    
    q.append([start_x-1, start_y-1, 0, 0])
    visited[start_x-1][start_y-1][0] = True
    
    while q:
        cur_x, cur_y, cnt, usable = q.popleft()
        
        if cur_x == end_x-1 and cur_y == end_y-1:
            global answer
            answer = min(answer, cnt)
            return
        
        for i in range(4):
            nx, ny = cur_x+dx[i], cur_y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny][usable]:
                    if board[nx][ny] == 0:    
                        visited[nx][ny][usable] = True
                        q.append([nx, ny, cnt+1, usable])
                    elif board[nx][ny] == 1:
                        if usable == 0:
                            visited[nx][ny][1] = True
                            q.append([nx,ny,cnt+1, 1])


if __name__ == "__main__":
    answer = 1e9
    
    n,m = map(int, input().split())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    bfs()
    
    if answer == 1e9:
        print(-1)
    else:
        print(answer)