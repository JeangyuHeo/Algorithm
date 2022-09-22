import heapq
from collections import defaultdict

def dijkstra(n, paths, gates, summits):
    pq = []
    global graph
    dist = [1e9 for _ in range(n+1)]
    
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        dist[gate] = 0
    summits.sort()
    summits_set = set(summits)
    
    while pq:
        intensity, node = heapq.heappop(pq)
        
        if node in summits_set or intensity > dist[node]:
            continue
    
        for weight, _next in graph[node]:
            new_intensity = max(intensity, weight)
            if new_intensity < dist[_next]:
                dist[_next] = new_intensity
                heapq.heappush(pq, (new_intensity, _next))
                
    min_intensity = [0, 1e9]

    for summit in summits:
        if dist[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = dist[summit]
                
    return min_intensity
    
def solution(n, paths, gates, summits):
    global graph
    graph = defaultdict(list)
    
    for _from, _to, intensity in paths:
        graph[_from].append((intensity, _to))
        graph[_to].append((intensity, _from))
    
    return dijkstra(n, paths, gates, summits)


if __name__ == "__main__":
    print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
    print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4]))
    print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3,7], [1,5]))
    print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],[1,2],[5]))