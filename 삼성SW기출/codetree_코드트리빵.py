from collections import deque
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
cvs = [tuple(map(int,input().split())) for _ in range(m)]
base_camp = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            base_camp.append((i,j))

start = []
for i, j in cvs:
    min_dist, min_idx = 1e9, -1
    for k in range(len(base_camp)):
        x, y = base_camp[k]
        cur_dist = abs(i-x-1)+abs(j-1-y)

        if cur_dist < min_dist and k not in start:
            min_dist = cur_dist
            min_idx = k
    
    start.append(min_idx)

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(n)]
complete = [0 for _ in range(m)]
cnt = 1
q = deque([(base_camp[start[0]][0], base_camp[start[0]][1], 0, 0)])
board[base_camp[start[0]][0]][base_camp[start[0]][1]] = 2
visited[base_camp[start[0]][0]][base_camp[start[0]][1]][0] = True

while q:
    if cnt < m:
        q.append((base_camp[start[cnt]][0], base_camp[start[cnt]][1], cnt, 0))
        board[base_camp[start[cnt]][0]][base_camp[start[cnt]][1]] = 2
        visited[base_camp[start[cnt]][0]][base_camp[start[cnt]][1]][cnt] = True
        cnt += 1

    x, y, no, time = q.popleft()
    
    if complete[no] != 0:
        continue

    if (x,y) == (cvs[no][0]-1, cvs[no][1]-1):
        board[x][y] = 2
        complete[no] = time
    
    if all([c for c in complete]):
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny][no]:
                if board[nx][ny] != 2:
                    visited[nx][ny][no] = True
                    q.append((nx,ny,no,time+1))

print(max([i+1+complete[i] for i in range(m)]))