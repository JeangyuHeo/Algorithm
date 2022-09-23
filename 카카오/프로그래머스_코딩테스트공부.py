def solution(alp, cop, problems):
    max_alp, max_cop, time = 0, 0, 0
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
        time += cost
        
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[1e9 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
                
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    n_alp, n_cop = min(max_alp, i+alp_rwd), min(max_cop, j+cop_rwd)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], dp[i][j] + cost)
                    
    return dp[-1][-1]

if __name__ == "__main__":
    print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
    print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))