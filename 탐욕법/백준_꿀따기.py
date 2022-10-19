import sys

input = sys.stdin.readline

if __name__ == "__main__":
    max_val = -1
    n = int(input())
    honey = list(map(int, input().split()))
    sum = [0 for _ in range(n)]
    
    for i in range(n):
        sum[i] += honey[i] + sum[i-1]
        
    
    for i in range(1, n-1):
        max_val = max(max_val, 2*sum[-1]-honey[0]-honey[i]-sum[i])
    
    for i in range(1, n-1):
        max_val = max(max_val, sum[-1]-honey[-1]-honey[i]+(sum[i-1]))
        
    for i in range(1, n-1):
        max_val = max(max_val, sum[i] - honey[0] + (sum[-1] - sum[i-1] - honey[-1]))
        
    print(max_val)