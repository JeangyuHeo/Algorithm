NUM_WAY = 4
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
row, col = map(int, input().split())

board = [input() for _ in range(row)]
visited = [[[[False]*col for _ in range(row)] for _ in range(col)] for _ in range(row)]

q = []

def move(cur_x, cur_y, move_x, move_y):
    count = 0
    
    while board[cur_x][cur_y] != 'O' and board[cur_x + move_x][cur_y + move_y] != '#':
        cur_x += move_x
        cur_y += move_y
        count += 1
        
    return cur_x, cur_y, count
    
def bfs():
    rx, ry, bx, by = [0] * 4
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
                
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    
    while q:
        rx, ry, bx, by, depth = q.pop(0)
        
        if depth > 10:
            break
        for i in range(NUM_WAY):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])
            
            if board[next_bx][next_by] =='O':
                continue
            if board[next_rx][next_ry] == 'O':
                print(depth)
                return
            
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth+1))
    
    print(-1)

bfs()