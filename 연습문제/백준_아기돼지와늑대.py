dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check_cant_go(answer, visited):
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and board[i][j] == '.':
                answer[i][j] = 'P'             
    
def bfs(wolves):
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    for wx, wy in wolves:
        visited[wx][wy] = True
        
    while wolves:
        x, y = wolves.pop(0)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            while 0<=nx<r and 0<=ny<c and board[nx][ny] =='+':
                if board[nx+dx[i]][ny+dy[i]] == '#':
                    break
                nx, ny = nx+dx[i], ny+dy[i]
                if board[nx][ny] in ['W', '.']:
                    break
            
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny] != '#':
                visited[nx][ny] = True
                wolves.append((nx, ny))
            
    return visited

if __name__ == "__main__":
    r, c = map(int, input().split())
    wolves=[]
    board = [input() for _ in range(r)]
    answer = [list(x) for x in board]

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'W':
                wolves.append((i,j))

    check_cant_go(answer, bfs(wolves)) 

    for row in answer:
        print(''.join(row))