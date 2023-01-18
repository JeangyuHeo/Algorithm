import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().strip().split())
        weight = list(map(int, input().strip().split()))
        printer = deque([(w, i) for i, w in enumerate(weight)])
        
        cnt = 0
        while printer:
            if printer[0][0] == max(printer, key = lambda x: x[0])[0]:
                cnt+=1
                if printer[0][1] == m:
                    break
                else:
                    printer.popleft()
            else:
                printer.append(printer.popleft())
    
        print(cnt)
    
        
        