import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    classes = sorted([list(map(int, input().split())) for _ in range(n)])
    
    pq = []
    heapq.heappush(pq, classes[0][1])
    
    for i in range(1, n):
        if classes[i][0] < pq[0]:
            heapq.heappush(pq, classes[i][1])
        else:
            heapq.heappop(pq)
            heapq.heappush(pq, classes[i][1])
    
    print(len(pq))