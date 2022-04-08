def check():

    for i in range(N):
        pos = i
        for j in range(H):
            if board[j][pos] == 1:
                pos += 1
            elif board[j][pos-1] == 1:
                pos -= 1
        if pos != i:
            return False
    
    return True

def dfs(depth, r, c):
    global answer
    if depth >= answer:
        return
    
    if check():
        answer = min(answer, depth)
        return
    
    if depth == 3:
        return
    
    for i in range(H):
        for j in range(N-1):
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
                board[i][j] = 1
                dfs(depth+1, i, j)
                board[i][j] = 0
            
        x = 0
    
    
if __name__ == "__main__":
    answer = 4
    # N 세로선 수, M 가로선 수, H 가로선 놓을 수 있는 위치의 수
    N, M, H = map(int, input().split(' '))
    
    if M == 0:
        print(0)
    else:
        board = [[0 for _ in range(N)] for _ in range(H)]
        
        for _ in range(M):
            a, b = map(int, input().split(' '))
            board[a-1][b-1] = 1
            
        dfs(0,0,0)
    
        print(-1 if answer > 3 else answer) 