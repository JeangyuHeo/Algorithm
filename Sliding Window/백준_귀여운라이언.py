import sys

input = sys.stdin.readline

if __name__ == "__main__":
    answer = 1e9
    n, k = map(int, input().split())
    dolls = list(map(int, input().strip().split()))
    lion_idx = []
    
    for i in range(n):
        if dolls[i] == 1:
            lion_idx.append(i)
    if len(lion_idx) < k:
        answer = -1
    else:
        for i in range(0, len(lion_idx)-k+1):
            answer = min(answer, lion_idx[i+k-1]-lion_idx[i]+1)
        
    print(answer)