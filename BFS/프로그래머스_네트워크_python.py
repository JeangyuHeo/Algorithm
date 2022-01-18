from collections import deque

def BFS(computers, i, visited):
    q = deque([i])
    
    while q:
        cur = q.popleft()
        visited[cur]=True
        
        for connected_node in range(len(computers)):
            if all([connected_node != cur, computers[connected_node][cur] == 1, visited[connected_node] == False]):
                q.append(connected_node)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for i in range(n):
        if not visited[i]:
            BFS(computers, i, visited)
            answer+=1
        
    return answer

print(solution(3, [[1,1,0], [1,1,0], [0,0,1]]))
print(solution(3, [[1,1,0], [1,1,1], [0,1,1]]))