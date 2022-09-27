import heapq
from collections import defaultdict

def dijkstra(start):
    dist = [1e9 for _ in range(n+1)]
    pq = []
    res = []

    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        cost, cur = heapq.heappop(pq)

        for next in con_dict[cur]:
            if cost + 1 < dist[next]:
                dist[next] = cost+1
                heapq.heappush(pq, (cost+1, next))
    
    for i in range(1, n+1):
        if dist[i] == k:
            res.append(i)

    if len(res) == 0:
        print(-1)
    else:
        for i in res:
            print(i)

if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    con_dict = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        con_dict[a].append(b)

    dijkstra(x)
