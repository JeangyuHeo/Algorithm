def is_over(board, mark):
    for i in range(3):
        if all([board[i][0] == mark, board[i][1] == mark, board[i][2] == mark]):
            return True
        if all([board[0][i] == mark, board[1][i] == mark, board[2][i] == mark]):
            return True
    if all([board[0][0] == mark, board[1][1] == mark, board[2][2] == mark]):
        return True
    if all([board[0][2] == mark, board[1][1] == mark, board[2][0] == mark]):
        return True
    return False

def solution(board):
    o_cnt, x_cnt = 0, 0
    
    for r in board:
        o_cnt += r.count("O")
        x_cnt += r.count("X")
    
    o_result = is_over(board, "O")
    x_result = is_over(board, "X")
    
    if x_cnt > o_cnt:
        return 0
    elif x_cnt == o_cnt:
        if o_result:
            return 0
        if x_result and not o_result:
            return 1
        
    if x_result and not o_result:
        return 0
    
    if o_result and x_result:
        return 0
    
    if abs(x_cnt - o_cnt) > 1:
        return 0
    
    return 1

if __name__ == "__main__":
    print(solution(["O.X", ".O.", "..X"]))
    print(solution(["OOO", "...", "XXX"]))
    print(solution(["...", ".X.", "..."]))
    print(solution(["...", "...", "..."]))