import sys, heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    pq = []
    
    for i in range(n):
        for j in range(n):
            heapq.heappush(pq, arr[i][j])
            if len(pq) > n:
                heapq.heappop(pq)
                
    print(min(pq))