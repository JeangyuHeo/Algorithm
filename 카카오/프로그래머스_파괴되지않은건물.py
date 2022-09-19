def solution(board, skill):
    row = len(board)
    col = len(board[0])
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
    answer = 0
    
    for t, r1, c1, r2, c2, degree in skill:
        dir = -1 if t == 1 else 1
        dp[r1][c1] += dir*degree
        dp[r2+1][c1] -= dir*degree
        dp[r1][c2+1] -= dir*degree
        dp[r2+1][c2+1] += dir*degree
        
    for r in range(row):
        for c in range(1, col):
            dp[r][c] += dp[r][c-1]
    
    for c in range(col):
        for r in range(1, row):
            dp[r][c] += dp[r-1][c]
            
    for r in range(row):
        for c in range(col):
            dp[r][c] += board[r][c]
            if dp[r][c] > 0:
                answer += 1

    return answer

if __name__ == "__main__":
    print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
    print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))