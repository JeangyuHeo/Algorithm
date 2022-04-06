
def solution(x, y, dx, dy):
    count = 1
    
    for _ in range(board_size-1):
        nx, ny = x + dx, y + dy
        diff = board[nx][ny] - board[x][y]
        
        if abs(diff) > 1:
            return 0
        if diff > 0: # 뒤가 더 큼
            if count >= length:
                count = 0
            else:
                return 0
            
        elif diff < 0: # 앞이 더 큼
            if count >= 0:
                count = -length
            else:
                return 0
            
        count += 1
        x = nx
        y = ny
    
    return 1 if count >=0 else 0

if __name__ == "__main__":
    answer = 0
    board_size, length = map(int, input().split(" "))
    board = [list(map(int, input().split(" "))) for _ in range(board_size)]
    
    for i in range(board_size):
        answer += solution(0, i, 1, 0)
        answer += solution(i, 0, 0, 1)
        
    print(answer)