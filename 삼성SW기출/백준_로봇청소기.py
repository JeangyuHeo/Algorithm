import sys
input = sys.stdin.readline

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(r, c, dir):
    global answer
    if not visited[r][c]:
        visited[r][c] = True
        answer += 1
                    
    for i in range(4):
        nd = (dir+3) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        
        if 0<nx<row-1 and 0<ny<col-1:
            if board[nx][ny] != 1:
                if not visited[nx][ny]:
                    dfs(nx, ny, nd)
                    return
        dir = nd
    back = (dir+2) % 4
    
    if board[r+dx[back]][c+dy[back]] == 1:
        return
    else:
        dfs(r+dx[back], c+dy[back], dir)
    

if __name__ == "__main__":
    answer = 0
    row, col = map(int, input().split(" "))
    start_row, start_col, dir = map(int, input().split(" "))
    visited = [[False for _ in range(col)] for _ in range(row)]
    board = []
    
    for _ in range(row):
        board.append(list(map(int, input().split(" "))))
        
    dfs(start_row, start_col, dir)
    print(answer)