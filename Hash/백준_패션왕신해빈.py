import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        answer = 1
        cloth_dict = defaultdict(int)
        n = int(input())
        for _ in range(n):
            _, category = input().split()
            cloth_dict[category]+= 1
        
        for v in cloth_dict.values():
            answer *= v+1
        print(answer - 1)