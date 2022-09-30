import numbers
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    global visited, num
    
    q = deque([(x,y)])
    visited[x][y] = num
    
    res  = 1

    while q:
        cur_x, cur_y = q.popleft()
        
        for i in range(4):
            nx, ny = cur_x+dx[i], cur_y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        res+=1
                        visited[nx][ny] = num
                        q.append((nx, ny))
    
    return res

if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    answer = 0
    block_dict = {}
    
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    num = 2
    
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1 and not visited[x][y]:
                res = bfs(x,y)
                block_dict[num] = res
                num += 1
    
    for x in range(n):
        for y in range(m):
            near_set = set()
            if board[x][y] == 0:
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<n and 0<=ny<m:
                        if board[nx][ny] == 1:
                            near_set.add(visited[nx][ny])
            
            tmp = 1
            
            for block in near_set:
                tmp+= block_dict[block]
                
            answer = max(tmp, answer)
    
    print(answer)