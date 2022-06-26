from collections import defaultdict

def recursive_sol(i):
    if dp[i] != 0:
        return dp[i]
    
    dp[i] = recursive_sol(i//p) + recursive_sol(i//q)
    return dp[i]
    
if __name__ == "__main__":
    n, p, q = map(int, input().split())
    dp = defaultdict(int)
    dp[0] = 1
    
    print(recursive_sol(n))