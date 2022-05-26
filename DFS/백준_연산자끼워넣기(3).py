
def dfs(exp, idx, ops):
    if idx == n:
        global max_answer, min_answer
        
        result = eval(exp)
        min_answer = min(min_answer, result)
        max_answer = max(max_answer, result)
        return
    
    pl, mi, mu, di = ops
    
    if pl > 0:
        dfs(exp+'+'+nums[idx], idx+1, [pl-1, mi, mu, di])
    if mi > 0:
        dfs(exp+'-'+nums[idx], idx+1, [pl, mi-1, mu, di])
    if mu > 0:
        dfs(exp+'*'+nums[idx], idx+1, [pl, mi, mu-1, di])
    if di > 0:
        dfs(exp+'//'+nums[idx], idx+1, [pl, mi, mu, di-1])
        
if __name__ == "__main__":
    min_answer = 1e9
    max_answer = -1e9
    
    n = int(input())
    nums = list(input().split())
    opers = list(map(int, input().split()))
    
    dfs(nums[0], 1, opers)
    
    print(max_answer)
    print(min_answer)