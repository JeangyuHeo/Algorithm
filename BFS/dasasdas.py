from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(grid, k):
    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    q = deque()

    visited[0][0] = True
    q.append([0, 0, k, 0, visited])

    while q:
        x, y, remain, num, vis = q.popleft()
        print(x,y,remain,num)
        if (x,y) == (n-1,m-1):
            global answer
            answer = num
            q= deque()
            q.append([0,0,k,0,visited])
            return

        if grid[x][y] == 'F':
            if remain == 0:
                continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not vis[nx][ny]:
                    if grid[nx][ny] != '#':
                        if remain != 0:
                            tmp_vis = deepcopy(vis)
                            tmp_vis[nx][ny] =True
                            q.append([nx, ny, remain-1, num,tmp_vis])
                    if grid[nx][ny] == '.':
                        tmp_vis = deepcopy(vis)
                        tmp_vis[nx][ny] = True
                        q.append([nx, ny,k, num+1,tmp_vis])

def dfs(grid, k, x, y, remain, num):
    global answer

    if (x,y) == (n-1, m-1):
        answer = min(answer, num)
        return True

    if grid[x][y] == 'F':
        if remain == 0:
            return False

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                if grid[nx][ny] != '#':
                    if remain != 0:
                        visited[nx][ny] =True
                        result = dfs(grid, k, nx, ny, remain-1, num)
                        visited[nx][ny] = False

                if grid[nx][ny] == '.' and not result:
                    visited[nx][ny] = True
                    dfs(grid, k, nx, ny, k, num+1)
                    visited[nx][ny] = False

    return False
global answer, visited, n, m
answer = 1e9
n, m = 3,4
visited = [[False for _ in range(m)] for _ in range(n)]

visited[0][0] = True

#dfs(["..FF", "###F", "###."], 4,0,0,4,0)
dfs([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6, 0, 0, 6, 0)         
#bfs([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6)
print(answer)