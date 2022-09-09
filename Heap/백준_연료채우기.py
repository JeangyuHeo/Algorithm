import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    hq = []
    for _ in range(n):
        heapq.heappush(hq, list(map(int, input().split())))
    l, p = map(int, input().split())
    
    move = []
    cnt = 0
    
    while p < l:
        while hq and hq[0][0] <= p:
            dist, gas = heapq.heappop(hq)
            heapq.heappush(move, [-1 * gas, dist])
            
        if not move:
            cnt = -1
            break
        
        gas, dist = heapq.heappop(move)
        p += -gas
        cnt+=1
    
    print(cnt)