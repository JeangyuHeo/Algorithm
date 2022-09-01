import sys

input = sys.stdin.readline

if __name__ == "__main__":
    
    n = int(input())
    max_dp = [[0 for _ in range(3)] for _ in range(n)]
    min_dp = [[0 for _ in range(3)] for _ in range(n)]
    
    for r in range(n):
        inputs = list(map(int, input().split()))
        for c in range(3):
            if r == 0:
                max_dp[0][c] = inputs[c]
                min_dp[0][c] = inputs[c]
                continue
            if c == 0:
                max_dp[r][c] = inputs[c] + max(max_dp[r-1][c], max_dp[r-1][c+1])
                min_dp[r][c] = inputs[c] + min(min_dp[r-1][c], min_dp[r-1][c+1])
            elif c == 1:
                max_dp[r][c] = inputs[c] + max(max_dp[r-1][c-1], max_dp[r-1][c], max_dp[r-1][c+1])
                min_dp[r][c] = inputs[c] + min(min_dp[r-1][c-1], min_dp[r-1][c], min_dp[r-1][c+1])
            elif c == 2:
                max_dp[r][c] = inputs[c] + max(max_dp[r-1][c], max_dp[r-1][c-1])
                min_dp[r][c] = inputs[c] + min(min_dp[r-1][c], min_dp[r-1][c-1])
        
    print(max(max_dp[n-1]), min(min_dp[n-1]))