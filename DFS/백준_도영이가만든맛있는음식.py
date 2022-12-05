import sys

input = sys.stdin.readline

def dfs(depth, start):
    global diff

    if depth == len_:
        sour = 1
        bitter = 0
        for i in arr:
            sour *= i[0]
            bitter += i[1]
        if abs(bitter - sour) < diff:
            diff = abs(bitter - sour)
        return

    for i in range(start, n):
        arr.append(things[i])
        dfs(depth + 1, i + 1)
        arr.pop()
    
if __name__ == "__main__":
    n = int(input())
    arr = []
    things = sorted(
                [list(map(int, input().split())) for _ in range(n)],
                key = lambda x: abs(x[0]-x[1])
            )
    
    diff = 1e9

    for i in range(1, n+1):
        len_ = i
        dfs(0, 0)
    print(diff)