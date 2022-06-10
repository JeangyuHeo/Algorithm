import heapq
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    
    dist = [1e9 for _ in range(N+1)]
    graph = defaultdict(list)
    
    for i,j, cost in road:
        graph[i].append([j,cost]) 
        graph[j].append([i,cost])
    
    dist[1] = 0
    
    pq = []
    
    heapq.heappush(pq, [0, 1])
    
    while pq:
        cur_dist, cur_idx = heapq.heappop(pq)

        for next_idx, cost in graph[cur_idx]:
            next_dist = cur_dist + cost
            if next_dist < dist[next_idx]:
                dist[next_idx] = next_dist
                heapq.heappush(pq, [next_dist, next_idx])
    
    for i in range(1, N+1):
        if dist[i] <= K:
            answer += 1
            
    return answer

if __name__ == "__main__":
    print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
    print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))