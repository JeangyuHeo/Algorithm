import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, num):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    q = deque()
    cnt = 1
    
    q.append((x, y))
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y +dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if board[nx][ny] == num:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
                        
    return cnt

if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    
    answer = 0
    n, m, k = map(int, input().split())
    dice = [1, 2, 3, 4, 5, 6]
    board = [list(map(int, input().split())) for _ in range(n)]
    
    x, y = 0, 0
    move = 1
    
    for _ in range(k):
        if x+dx[move] < 0 or x+dx[move] >= n or y+dy[move] < 0 or y+dy[move] >= m:
            move = (move + 2) % 4
        
        x, y = x+dx[move], y+dy[move]
        
        answer += bfs(x, y, board[x][y]) * board[x][y]
        
        if move == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif move == 2:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        elif move == 3:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

        if dice[5] < board[x][y]:
            move = (move+3) % 4
        elif dice[5] > board[x][y]:
            move = (move+1) % 4
    
    print(answer)