dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


def check_near(x,y):
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] == '*':
                return False
    return True

def dfs(x, y):

    board[x][y] = '#'
        
    if not check_near(x, y):
        return
        
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] == '.':
                dfs(nx,ny)

T = int(input())

def count_solo():
    global answer
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                
                answer+=1
                
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    board = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                if check_near(i,j):
                    dfs(i,j)
                    answer+=1
                    
    count_solo()
    
    print(f"#{test_case} {answer}")