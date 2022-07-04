import sys
import heapq

input = sys.stdin.readline
    
if __name__ == "__main__":
    answer = 0
    n, k = map(int, input().split())    
    jewels = sorted([list(map(int, input().split())) for _ in range(n)])
    limit = sorted([int(input()) for _ in range(k)])
    heap = []

    for l in limit:
        while jewels and l >= jewels[0][0]:
            heapq.heappush(heap, -jewels[0][1])
            heapq.heappop(jewels)
            
        if heap:
            answer += heapq.heappop(heap)
        elif not jewels:
            break
    
    print(-answer)