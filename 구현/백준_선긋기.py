import sys

input = sys.stdin.readline

if __name__ == "__main__":
    answer = 0
    n = int(input())
    lines = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    
    cur = lines[0]
    merged = []
    
    for i in range(1, n):
        if lines[i][0] <= cur[1]:
            cur[1] = max(cur[1], lines[i][1])
        else:
            answer += cur[1] - cur[0]
            cur = lines[i]
    
    answer += cur[1] - cur[0]
    
    print(answer)