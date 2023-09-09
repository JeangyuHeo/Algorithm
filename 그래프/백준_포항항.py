from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_idx(x,y):
    for i in range(len(total)):
        if [x,y] == total[i]:
            return i
    return -1
        
    
def bfs(start_x, start_y, idx):
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    q = deque()
    
    q.append([start_x, start_y, 0])
    visited[start_x][start_y] = True
    
    while q:
        cur_x, cur_y, cost = q.popleft()
        
        if board[cur_x][cur_y] == 'K':
            _idx = find_idx(cur_x, cur_y)
            dist[idx][_idx] = cost
            dist[_idx][idx] = cost
        
        for i in range(4):
            nx, ny = cur_x+dx[i], cur_y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] != 'X':
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny, cost+1])
    
def find_restaurants():
    result = []
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                global start
                start = [i, j]
            elif board[i][j] == 'K':
                result.append([i,j])
                
    return result

def dfs(cnt, prev, sum):
    global answer
    print(prev)
    if cnt == 5:
        answer =min(answer, sum)
        return
    
    for i in range(len(dist)):
        if visited[i]:
            continue
        new_cost = sum+dist[prev][i]
        if new_cost > answer:
            continue
        else:
            visited[i] = True
            dfs(cnt+1, i, new_cost)
            visited[i] = False
   
if __name__ == "__main__":
    answer = 1e9
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    start = []
    restaurants = find_restaurants()
    total = [start]+ restaurants
    dist = [[1e9 for _ in range(len(total))] for _ in range(len(total))]
    dist[0][0] = 0
    dist[-1][-1] = 0
    
    for i in range(len(total)-1):
        x,y = total[i][0], total[i][1]
        bfs(x, y, i)

    visited=[False for _ in range(len(dist))]
    visited[0] = True
    dfs(0,0,0)
    
    if answer == 1e9:
        print(-1)
    else:
        print(answer)
    
"""
4 4
SKKK
KXXK
KKX.
KKXK
"""

