import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    height = sorted(list(map(int, input().split())))
    print(sum(sorted([height[i]-height[i-1] for i in range(1, n)])[:n-k]))