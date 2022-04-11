dy = (0,-1,0,1)
dx = (1,0,-1,0)

def count_square():
    answer = 0
    
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
                answer += 1

    return answer

if __name__ == "__main__":
    N = int(input())     
    board = [[0 for _ in range(101)] for _ in range(101)]
    
    for _ in range(N):
        x, y, d, g = map(int, input().split(' '))
        
        board[y][x] = 1
        
        move = [d]
        
        for _ in range(g):
            tmp = []
            
            for i in move[::-1]:
                tmp.append((i+1)%4)
            move.extend(tmp)
    
        for i in move:
            nx = x + dx[i]
            ny = y + dy[i]
            board[ny][nx] = 1
            x, y = nx, ny
            
    print(count_square())