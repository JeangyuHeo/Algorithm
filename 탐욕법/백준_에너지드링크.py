import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    print('%g'%sum([num / 2 if idx != n-1 else num for idx, num in enumerate(sorted(list(map(int, input().split()))))]))