import sys

input = sys.stdin.readline

def solution():
    
    for idx in range(n-1, -1, -1):
        if idx + schedule[idx][0] > n:
            dp[idx] = dp[idx+1]
        else:
            dp[idx] = max(schedule[idx][1] + dp[idx + schedule[idx][0]], dp[idx+1])

    print(max(dp))
    
if __name__ == "__main__":
    n = int(input())
    schedule = []
    answer = 0
    dp = [0 for _ in range(n+1)]

    for _ in range(n):
        schedule.append(list(map(int, input().split(' '))))

    solution()