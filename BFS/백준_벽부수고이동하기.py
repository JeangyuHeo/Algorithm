from collections import deque

def bfs():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    q = deque()
    
    q.append([0,0,1,0])
    
    while q:
        x, y, cnt, usable = q.popleft()
        
        if (x,y) == (n-1,m-1):
            return cnt
    
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny][usable]:
                    if board[nx][ny] == '0':
                        q.append([nx,ny,cnt+1,usable])
                        visited[nx][ny][usable] = True
                    else:
                        if usable == 0:
                            q.append([nx,ny,cnt+1,1])
                            visited[nx][ny][1] = True
    
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    
    print(bfs())