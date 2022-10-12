import sys

input = sys.stdin.readline

def dfs(x, y, d):
    global answer
    
    if not visited[x][y]:
        visited[x][y] = True
        answer += 1
    
    for _ in range(4):
        nd = (d + 3) % 4
        nx, ny = x+dx[nd], y+dy[nd]
        
        if 0<nx<n-1 and 0<ny<m-1:
            if not visited[nx][ny]:
                if board[nx][ny] == 0:
                    dfs(nx, ny, nd)
                    return
    
        d = nd
    back = (d+2) % 4
    if board[x+dx[back]][y+dy[back]] == 1:
        return
    else:
        dfs(x+dx[back], y+dy[back], d)

if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    
    answer = 0
    n, m = map(int, input().split())
    p_x, p_y, dir = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    dfs(p_x, p_y, dir)
    
    print(answer)