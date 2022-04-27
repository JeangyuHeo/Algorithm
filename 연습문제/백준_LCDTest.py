def make_board():
    return [[' ' for _ in range(s+3)] for _ in range(2*s+3)]

def draw_row_first(board):
    for i in range(1, s+1):
        board[0][i] = '-'
        
def draw_row_second(board):
    for i in range(1,s+1):
        board[s+1][i] = '-'
    
def draw_row_third(board):
    for i in range(1, s+1):
        board[2*s + 2][i] = '-'
        
def draw_col_top_left(board):
    for i in range(1, s+1):
        board[i][0] = '|'

def draw_col_top_right(board):
    for i in range(1, s+1):
        board[i][-2] = '|'
 
def draw_col_bot_left(board):
        for i in range(s+2, 2*s+2):
            board[i][0] = '|'

def draw_col_bot_right(board):
    for i in range(s+2, 2*s+2):
        board[i][-2] = '|'       

def draw_number(num):
    board = make_board()
    
    if num in [0,2,3,5,6,7,8,9]:
        draw_row_first(board)
    if num in [0,4,5,6,8,9]:
        draw_col_top_left(board)
    if num in [0,1,2,3,4,7,8,9]:
        draw_col_top_right(board)
    if num in [2,3,4,5,6,8,9]:
        draw_row_second(board)
    if num in [0,2,6,8]:
        draw_col_bot_left(board)
    if num in [0,1,3,4,5,6,7,8,9]:
        draw_col_bot_right(board)
    if num in [0,2,3,5,6,8,9]:
        draw_row_third(board)
        
    return board        
    
if __name__ == "__main__":
    s, n = map(int, input().split())
    str_n = str(n)
    
    answer = [[] for _ in range(2 * s + 3)]

    for ch in str_n:
        board = draw_number(int(ch))
        for idx, row in enumerate(board):
            answer[idx].extend(row)
            
    for row in answer:
        print(''.join(row[:-1]))