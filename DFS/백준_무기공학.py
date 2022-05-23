move = [
    [0, -1, 1, 0],
    [-1, 0, 0, -1],
    [-1, 0, 0, 1],
    [1, 0, 0, 1],
]

def check_range(i, x, y):
    f_x, f_y, s_x, s_y = move[i]
    
    if 0 <= x + f_x < n and 0 <= y + f_y < m and 0 <= x + s_x < n and 0 <= y + s_y < m:
        return True
    else:
        return False
    
def check_visited(i,x,y):
    f_x, f_y, s_x, s_y = move[i]
    return not visited[x][y] and not visited[x+f_x][y+f_y] and not visited[x+s_x][y+s_y]
        
def calc_score(i, x, y):
    f_x, f_y, s_x, s_y = move[i]
    return board[x+f_x][y+f_y] + board[x+s_x][y+s_y] + 2*board[x][y]

def control_visited(i, x, y):
    f_x, f_y, s_x, s_y = move[i]
    
    visited[x][y] = not visited[x][y]
    visited[x+f_x][y+f_y] = not visited[x+f_x][y+f_y]
    visited[x+s_x][y+s_y] = not visited[x+s_x][y+s_y]
        
def dfs(x, y, score):
    if y == m:
        x += 1
        y = 0
        
    if x == n:
        global answer
        answer = max(answer, score)
        return

    if not visited[x][y]:
        for i in range(4):
            if check_range(i, x, y):
                if check_visited(i,x,y):
                    update_score = score + calc_score(i, x, y)
                    control_visited(i,x,y)
                    dfs(x, y+1, update_score)
                    control_visited(i,x,y)
    
    dfs(x,y+1,score)
            

if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    dfs(0,0,0)
    
    print(answer)