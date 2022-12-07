import sys

input = sys.stdin.readline

def solution():
    global answer
    
    for lamp in lamps:
        zero_count = lamp.count(0)
        if zero_count <= k and zero_count%2 == k%2:
            cnt = 0
            for j in lamps:
                if j == lamp:
                    cnt += 1
            answer = max(answer, cnt)

if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().strip().split())
    lamps = [list(map(int, input().strip())) for _ in range(n)]
    k = int(input())

    solution()
    
    print(answer)