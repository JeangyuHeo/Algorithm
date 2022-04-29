import heapq

def get_smallest_index(dist, visited):
    min = 1e9
    idx = -1
    
    for i in range(6):
        if dist[i] < min and not visited[i]:
            min = dist[i]
            idx = i
        
    return idx

def dijkstra_1(start: int):
    graph = [
        [0,2,5,1,1e9,1e9],
        [2,0,3,2,1e9,1e9],
        [5,3,0,3,1,5],
        [1,2,3,0,1,1e9],
        [1e9,1e9,1,1,0,2],
        [1e9,1e9,5,1e9,2,0],    
    ]
    visited = [False for _ in range(6)]
    dist = [1e9 for _ in range(6)]
    
    for i in range(6):
        dist[i] = graph[start][i]
        
    visited[start] = True
    
    for i in range(6):
        cur = get_smallest_index(dist, visited)
        visited[cur] = True
        
        for j in range(6):
            if not visited[j]:
                if dist[cur] + graph[cur][j] < dist[j]:
                    dist[j] = dist[cur] + graph[cur][j]
    print(dist)

def dijkstra_2(start: int):
    graph = [
        [0,2,5,1,1e9,1e9],
        [2,0,3,2,1e9,1e9],
        [5,3,0,3,1,5],
        [1,2,3,0,1,1e9],
        [1e9,1e9,1,1,0,2],
        [1e9,1e9,5,1e9,2,0],    
    ]
    visited = [False for _ in range(6)]
    dist = [1e9 for _ in range(6)]
    
    pq = []
    dist[start] = 0
    visited[start] = True
    
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_dis, cur_idx = heapq.heappop(pq)

        if dist[cur_idx] < cur_dis:
            continue
        for i in range(6):
            if graph[cur_idx][i] != 1e9:
                next_dist = cur_dis + graph[cur_idx][i]
                if next_dist < dist[i]:
                    dist[i] = next_dist
                    heapq.heappush(pq, (next_dist, i))
        
    print(dist)

if __name__ == "__main__":
    dijkstra_1(0)
    dijkstra_2(0)