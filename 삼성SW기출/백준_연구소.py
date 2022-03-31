import sys
from copy import deepcopy

input = sys.stdin.readline

def init_virus_list():
    for i in range(row):
        for j in range(col):
            if board[i][j] == 2:
                virus_list.append((i,j))
    
def spread_virus():
    temp = deepcopy(board)
    q = deepcopy(virus_list)
    
    while q:
        x, y = q.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<row and 0<=ny<col:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))
    
    global answer
    
    result = sum(i.count(0) for i in temp)    
    answer = max(answer, result)

def make_wall(start, count):
    if count == 3:
        spread_virus()
        return
    
    for i in range(start, row * col):
        r = i // col
        c = i % col
        if board[r][c] == 0:
            board[r][c] = 1
            make_wall(i, count+1)
            board[r][c] = 0
    
if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    
    answer = 0
    row, col = map(int, input().split(' '))
    board = [list(map(int, input().split(' '))) for _ in range(row)]
    
    virus_list = []
    
    init_virus_list()
    make_wall(0,0)
    print(answer)