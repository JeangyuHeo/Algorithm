from collections import deque
from copy import deepcopy

def dfs(board, x, y, l_scroll, r_scroll):
    
    if (x,y) == (r-1, c-1):
        print("YES")
        exit(0)
    
    cur = info[board[x][y]]
    
    nx, ny = x+dx[cur], y+dy[cur]
    
    if 0<=nx<r and 0<=ny<c:
        if not visited[x][y][cur]:
            visited[x][y][cur] = True
            dfs(board, nx,ny,l_scroll,r_scroll)
            
    if l_scroll == 1:
        left_turn = (cur + 1) % 4
        nx, ny = x+dx[left_turn], y+dy[left_turn]
        
        if 0<=nx<r and 0<=ny<c:
            if not visited[x][y][left_turn]:
                visited[x][y][left_turn] = True
                tmp = deepcopy(board)
                tmp[x][y] = rev_info[left_turn]
                dfs(tmp, nx, ny, 0, r_scroll)
                
    if r_scroll == 1:
        right_turn = (cur - 1) % 4
        nx, ny = x+dx[right_turn], y+dy[right_turn]
        
        if 0<=nx<r and 0<=ny<c:
            if not visited[x][y][right_turn]:
                visited[x][y][right_turn] = True
                tmp = deepcopy(board)
                tmp[x][y] = rev_info[right_turn]
                dfs(tmp, nx, ny, l_scroll, 0)
        
    
if __name__ == "__main__":
    dx = [-1, 0 ,1 , 0]
    dy = [0, 1, 0 , -1]
    info = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    rev_info = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}
    
    r,c,k = map(int, input().split())
    maze = [list(input()) for _ in range(r)]
    visited = [[[False for _ in range(4)] for _ in range(c)] for _ in range(r)]
    
    dfs(maze,0,0,k,k)
    print("No")