from functools import reduce
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global boss_hp
    q=deque()
    visited = [[[False for _ in range(p)] for _ in range(n)] for _ in range(m)]
    arrived = []
    
    for x,y,player in player_pos:
        q.append((x,y,player))
        visited[x][y][player_idx[player]] = True
        
    while boss_hp > 0:
        for _ in range(len(q)):
            x,y,player = q.popleft()
            idx = player_idx[player]
            
            if board[x][y] == 'B':
                arrived.append(player)
                continue
            
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if ((not visited[nx][ny][idx]) and (board[nx][ny] != 'X')):
                        q.append((nx, ny, player))
                        visited[nx][ny][idx]= True
        
        if arrived:
            boss_hp -= reduce(lambda acc, cur: acc + player_dps[cur], arrived, 0)

    print(len(arrived))

def find_players():
    
    for i in range(m):
        for j in range(n):
            if 'a' <= board[i][j] <= 'z':
                player_pos.append((i,j,board[i][j]))
        
if __name__ == "__main__":
    m,n,p = map(int, input().split())
    board = [input() for _ in range(m)]
    player_dps = {}
    player_pos = []
    player_idx = {}
    
    for idx in range(p):
        player, dps = input().split()
        player_dps[player] = int(dps)
        player_idx[player]=idx
        
    boss_hp = int(input())
    
    find_players()
    
    bfs()