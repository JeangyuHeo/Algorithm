import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    schedule = []

    for _ in range(n):
        schedule.append(list(map(int, input().split(' '))))

    print(n, schedule)