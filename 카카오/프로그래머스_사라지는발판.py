dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
    
def game(board, aloc, bloc):
    global row, col
    answer = -1
    res = []
    
    if board[bloc[0]][bloc[1]] == 0:
        return True, 0
    if board[aloc[0]][aloc[1]] == 0:
        return False, 0
    
    
    for i in range(4):
        naloc = (aloc[0] + dx[i], aloc[1] + dy[i])
        
        
        if 0<=naloc[0]< row and 0<=naloc[1] < col:
            next_block = board[naloc[0]][naloc[1]]

            if next_block == 1:
                board[aloc[0]][aloc[1]] = 0
                win, time = game(board, bloc, naloc)
                board[aloc[0]][aloc[1]] = 1
                res.append((not win, time+1))
                
    if len(res) == 0:
        return False, 0
    elif any(r[0] for r in res):
        return True, min(r[1] for r in res if r[0])
    else:
        return False, max(r[1] for r in res)

def solution(board, aloc, bloc):
    global row, col
    row, col = len(board), len(board[0])
    return game(board, aloc, bloc)[1]

if __name__ == "__main__":
    print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1,0], [1,2]))
    print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1,0], [1,2]))
    print(solution([[1, 1, 1, 1, 1]], [0,0], [0,4]))
    print(solution([[1]], [0,0], [0,0]))