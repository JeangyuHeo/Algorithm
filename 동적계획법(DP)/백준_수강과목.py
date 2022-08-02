if __name__ == "__main__":
    n, k = map(int, input().split())
    dp =[[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(k):
        val, time = map(int, input().split())
        for j in range(1, n+1):
            if time <= j:
                dp[i+1][j] = max(dp[i][j], dp[i][j-time]+val)
            else:
                dp[i+1][j] = dp[i][j]
                
    print(dp[k][n])