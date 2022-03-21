from collections import deque

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def change(d, c):
    if c == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4
        
    return d

def check(y, x):
    if  (0<y<n+1) and (0<x<n+1) and (board[y][x] != 2):
        return True
    else:
        return False
    
def solution():
    direction = 1
    time = 1
    y, x = 1, 1
    visited = deque([[y, x]])
    board[y][x] = 2
    
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if check(y,x):
            if board[y][x] != 1:
                tail_y, tail_x = visited.popleft()
                board[tail_y][tail_x] = 0
            board[y][x] = 2
            visited.append([y,x])
            
            if time in info.keys():
                direction = change(direction, info[time])
            time += 1
        else:
            return time
        
if __name__ == "__main__":
    n = int(input())
    k = int(input())

    board = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split(' '))
        board[x][y] = 1
        
    l = int(input())
    info = {}
    for _ in range(l):
        num, dir = input().split(' ')
        info[int(num)] = dir
        
    print(solution())