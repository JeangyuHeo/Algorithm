from copy import deepcopy

def update(temp_board, type, x, y):
    for i in type:
        nx = x
        ny = y
        
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                break
            if temp_board[nx][ny] == 6:
                break
            elif temp_board[nx][ny] == 0:
                temp_board[nx][ny] = -1
    
def dfs(depth, temp_board):
    global answer
    
    if depth == num_cctv:
        answer = min(answer, sum([temp_board[i].count(0) for i in range(row)]))
        return
    
    backup = deepcopy(temp_board)
    r, w, cctv_type = cctv[depth]
    
    for mode in rotate_mode[cctv_type]:
        update(backup, mode, r, w)
        dfs(depth+1, backup)
        backup = deepcopy(temp_board)

if __name__ == "__main__":
    rotate_mode = [
        [],
        [[0], [1], [2], [3]],
        [[0,2], [1,3]],
        [[0,1], [1,2], [2,3], [3,0]],
        [[0, 1, 2], [1,2,3], [2,3,0], [3,0,1]],
        [[0,1,2,3]]
    ]
    
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    answer = 1e9
    
    row, col = map(int, input().split(" "))
    board = [list(map(int, input().split(" "))) for _ in range(row)]
    cctv = [(i,j,board[i][j])  for i in range(row) for j in range(col) if 0<board[i][j]<6]
    num_cctv = len(cctv)
    
    dfs(0, board)
    
    print(answer)