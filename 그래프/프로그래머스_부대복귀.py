import heapq
from collections import defaultdict

def dijkstra(n, graph, sources, destination):
    dist = [1e9 for _ in range(n)]
    
    dist[destination] = 0
    hq = [(0, destination)]
    
    while hq:
        cost, node = heapq.heappop(hq)
        
        for next_node in graph[node]:
            if dist[next_node] > cost + 1:
                dist[next_node] = cost + 1
                heapq.heappush(hq, (cost+1, next_node))
    
    return [dist[source-1] if dist[source-1] != 1e9 else -1 for source in sources]
        
def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    
    for start, end in roads:
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)
    
    return dijkstra(n, graph, sources, destination-1)


if __name__ == "__main__":
    print(solution(3, [[1, 2], [2, 3]], [2, 3], 1), [1, 2])
    print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5), [2, -1, 0])