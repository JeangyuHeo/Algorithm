from sys import exit
from collections import defaultdict, deque

if __name__ == "__main__":
    answer = []
    n,m,x,y = map(int, input().split())
    graph = defaultdict(set)
    q = deque()
    visited = [[False for _ in range(n+1)] for _ in range(y+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    q.append([x, 0])
    visited[0][x] = True
    
    while q:
        cur, cnt = q.popleft()
        
        if cnt == y:
            if cur not in answer:
                answer.append(cur)
        else:
            for next in graph[cur]:
                if not visited[cnt+1][next]:
                    visited[cnt+1][next]=True
                    q.append([next, cnt+1])

    if answer:
        for num in sorted(answer):
            print(num, end=' ')
    else:
        print(-1)