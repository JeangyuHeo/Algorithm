dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(i, x, y):
    visited = []
    nx, ny = x, y
    
    while True:
        nx, ny = nx+dx[i], ny+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == '.':
            board[nx][ny] = '!'
            visited.append([nx,ny])
        else:
            nx -= dx[i]
            ny -= dy[i]
            break
        
    return nx,ny,visited
        
def check_finish():
    for i in range(n):
        for j in range(m):
            if board[i][j]=='.':
                return False
    return True
                
def dfs(x, y,count):

    if check_finish():
        global answer
        answer = min(answer, count)
        return
    
    if count >= answer:
        return
    
    for i in range(4):
        f_x, f_y, visited = move(i, x, y)
        if visited:
            dfs(f_x, f_y,count+1)
        
        for r,c in visited:
            board[r][c] = '.'
    board[x][y] = '.'           
    
if __name__ == "__main__":
    recur = 1
    
    while True:
        try:
            answer = 1e9

            n, m = map(int, input().split())
            board = [list(input()) for _ in range(n)]
            
            for r in range(n):
                for c in range(m):
                    if board[r][c] == '.':
                        board[r][c] = '!'
                        dfs(r,c, 0)
                        
            if answer == 1e9:
                answer = -1
            print("Case {}: {}".format(recur, answer))
            recur+=1
        except:
            break