import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(start):
    visited = [False for _ in range(n+1)]
    dist = [1e9 for _ in range(n+1)]
    
    dist[start] = 0
    visited[start] = True
    
    pq = []
    heapq.heappush(pq, (0,start))
    
    while pq:
        cur_dist, cur_idx = heapq.heappop(pq)
        
        for node, cost in edges[cur_idx]:
            next_dist = cur_dist + cost
            if next_dist < dist[node]:
                dist[node] = next_dist
                heapq.heappush(pq, (next_dist, node))
                
    return dist
        

if __name__ == "__main__":
    n, e = map(int, input().split())
    edges = defaultdict(list)
    
    for _ in range(e):
        node1, node2, cost = map(int, input().split())
        
        edges[node1].append([node2, cost])
        edges[node2].append([node1, cost])
    
    start, end = map(int, input().split())
    
    d1 = dijkstra(1)
    d2 = dijkstra(start)
    d3 = dijkstra(end)
    
    ans = min(d1[start]+d2[end]+d3[n], d1[end]+d3[start]+d2[n])
    if ans >= 1e9:
        print(-1)
    else:
        print(ans)