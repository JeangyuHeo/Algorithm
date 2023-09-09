import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, l = map(int, input().strip().split())
    info = [tuple(map(int, input().strip().split())) for _ in range(n)]
    
    cur, answer = 0, 0
    
    for d, r, g in info:
        answer += d - cur
        
        cur = d
        
        if answer % (r+g) <= r:
            answer += r - (answer % (r+g))
            
    print(answer + l - info[-1][0])