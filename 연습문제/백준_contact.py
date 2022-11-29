import re
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input().strip())
    pattern = re.compile(("(100+1+|01)+"))
    
    for _ in range(T):
        message = input().strip()
        
        if pattern.fullmatch(message):
            print("YES")
        else:
            print("NO")