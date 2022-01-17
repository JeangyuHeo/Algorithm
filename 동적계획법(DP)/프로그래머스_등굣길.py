def solution(m, n, puddles):
    maps = [[0]*101 for i in range(101)]
    dp = [[0]*101 for i in range(101)]
    answer = 0
    
    for puddle in puddles:
        maps[puddle[1]][puddle[0]] = -1
    
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            elif maps[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            
    return dp[n][m]

print(solution(4,3,[[2,2]]))