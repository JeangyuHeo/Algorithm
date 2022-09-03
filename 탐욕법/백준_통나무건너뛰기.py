import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        answer = -1
        n = int(input())
        height = sorted(list(map(int, input().split())))
        
        q = deque()
        
        for i, h in enumerate(height[::-1]):
            if i % 2 == 0:
                q.append(h)
            else:
                q.appendleft(h)
            
        for i in range(len(q)-1):
            answer = max(answer, abs(q[i]- q[i-1]), abs(q[i]- q[i+1]))
        print(answer)