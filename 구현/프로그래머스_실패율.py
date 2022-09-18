from collections import defaultdict

def get_failrate(N, stage_list, dp):
    res = []
    for i in range(1, N+1):
        if dp[i] == 0:
            dp[i] = 1
        res.append([stage_list[i]/dp[i], i])
    return sorted(res, key=lambda x: -x[0])

def solution(N, stages):
    answer = []
    
    stage_list = [0 for _ in range(N+2)]
    dp = [0 for _ in range(N+2)] 
    
    for stage in stages:
        stage_list[stage] += 1
    
    dp[N+1] = stage_list[N+1]
    for i in range(N, 0, -1):
        dp[i] = dp[i+1] + stage_list[i]
    
    return [stage for rate, stage in get_failrate(N, stage_list, dp)]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(4, [2, 2, 2, 2, 2, 2]))