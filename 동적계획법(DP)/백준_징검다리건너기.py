import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    stone = list(map(int, input().strip().split()))
    dp = [0] + [1e9 for _ in range(n-1)]
    
    for i in range(1, n):
        for j in range(0, i):
            effort = max(dp[j], (i-j) * (1+abs(stone[i]-stone[j])))
            dp[i] = min(effort, dp[i])
            
    print(dp[-1])