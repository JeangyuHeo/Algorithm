import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0 for _ in range(31)]
    dp[1], dp[2] = 1, 3
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
        
    if n>=3:
        if n%2:
            print((dp[n] - dp[(n-1)//2]) // 2 + dp[(n-1)//2])
        else:
            print((dp[n]-(2*dp[(n-2)//2] + dp[n//2]))//2 + (2*dp[(n-2)//2] + dp[n//2]))
    else:
        print(dp[n])