dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)



def move_dice(num:int):
    if num == 1:
        tmp = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp
        
    elif num == 2:
        tmp = dice[3]
        dice[3] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = tmp
        
    elif num == 3:
        tmp = dice[3]
        dice[3] = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp
        
    elif num == 4:
        tmp = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[0]
        dice[0] = tmp
        
if __name__ == "__main__":
    row, col, start_x, start_y, k = map(int, input().split(' '))
    dice = [0] * 6
    board = []
    
    for i in range(row):
        board.append(list(map(int, input().split(' '))))
    command = list(map(int, input().split(' ')))
    
    for com in command:
        if not (0<=start_x + dx[com-1]<row and 0<=start_y +dy[com-1]<col):
            continue
        start_x += dx[com-1]
        start_y += dy[com-1]
        move_dice(com)
        
        if board[start_x][start_y] == 0:
            board[start_x][start_y] = dice[3]
        else:
            dice[3] = board[start_x][start_y]
            board[start_x][start_y] = 0

        print(dice[1])