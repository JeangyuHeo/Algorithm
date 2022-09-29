import copy
from collections import deque

def make_combs(cur, comb):
    if cur == len(possible):
        if len(comb) == 2:
            combs.append(comb)
        return
    if len(comb) > 2:
        return
    make_combs(cur+1, comb+[possible[cur]])
    make_combs(cur+1, comb)
def kill_black(grid, y, x):
    global answer
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    path = [(y, x)]
    flag = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if grid[ny][nx] == 0:
                    flag = False
                elif grid[ny][nx] == 2:
                    visited[ny][nx] = True
                    path.append((ny, nx))
                    q.append((ny, nx))
    if flag:
        answer += len(path)

if __name__ == "__main__": 
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    possible = []
    black = []
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                possible.append((i, j))
            if grid[i][j] == 2:
                black.append((i, j))
    combs = []
    ans = 0
    make_combs(0, [])
    for comb in combs:
        answer = 0
        tmp_grid = copy.deepcopy(grid)
        for i in range(2):
            tmp_grid[comb[i][0]][comb[i][1]] = 1
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2 and not visited[i][j]:
                    kill_black(tmp_grid, i, j)
        ans = max(ans, answer)
    print(ans)