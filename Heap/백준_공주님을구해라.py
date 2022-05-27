from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

if __name__ == "__main__":
    answer = 1e9
    n,m,t = map(int, input().split())
    castle = [list(map(int, input().split())) for _ in range(n)]
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    q = deque()
    
    q.append([0,0,0,0])
    
    while q:
        x, y, dist, sword = q.popleft()
        
        if dist > t:
            print("Fail")
            exit(0)
        
        if x == n-1 and y==m-1:
            print(dist)
            exit(0)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0<=nx<n and 0<=ny<m :
                if sword==1:
                    if not visited[nx][ny][sword]:
                        visited[nx][ny][sword] = True
                        q.append([nx,ny,dist+1,sword])
                else:
                    if castle[nx][ny] != 1 and not visited[nx][ny][sword]:
                        if castle[nx][ny] == 2:
                            sword += 1
                        q.append([nx,ny,dist+1,sword])
                        visited[nx][ny][sword] = True
    print("Fail")