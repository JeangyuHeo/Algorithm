import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [[-1001 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        _input = list(map(int, input().split()))
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + _input[j-1]
    
    answer = dp[0][0]
    
    for win_size in range(n):
        for i in range(1, n-win_size+1):
            for j in range(1, n-win_size+1):
                answer = max(answer, dp[i+win_size][j+win_size] - dp[i-1][j+win_size] - dp[i+win_size][j-1] + dp[i-1][j-1])

    print(answer)