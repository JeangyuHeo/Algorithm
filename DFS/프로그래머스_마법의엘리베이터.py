import sys

sys.setrecursionlimit(10**6)

def solution(storey):
    answer = 1e9
    
    def dfs(storey, cnt):
        nonlocal answer
            
        if storey <= 1:
            if storey == 1:
                cnt += 1
            answer = min(answer, cnt)
            return
        
        dfs(storey // 10, cnt + storey % 10)
        dfs((storey+10) // 10, cnt + (10 - (storey % 10)))
    
    dfs(storey, 0)
    
    return answer