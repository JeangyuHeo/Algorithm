import heapq

def dijkstra(start: int):
    visited = [False for _ in range(n+1)]
    dist = [1e9 for _ in range(n+1)]
    
    pq = []
    dist[start] = 0        
    visited[start] = True
    
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        
        if dist[cur_node] < cur_dist:
            continue
        for i in range(1, n+1):
            if graph[cur_node][i] != 1e9:
                next_dist = dist[cur_node] + graph[cur_node][i]
                if next_dist < dist[i]:
                    dist[i] = next_dist
                    heapq.heappush(pq, (next_dist, i))
    
    print(dist[t])
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s, t = map(int, input().split())
    graph = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
    
    for start, end, cost in edges:
        graph[start][end] = cost
        graph[end][start] = cost
    
    
    dijkstra(s)
    