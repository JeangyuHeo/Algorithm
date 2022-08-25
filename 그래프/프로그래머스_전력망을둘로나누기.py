from collections import deque

def solution(n, wires):
    node_map = [[0 for _ in range(n+1)] for _ in range(n+1)]
    answer = 1e9
    
    for parents, child in wires:
        node_map[parents][child] = 1
        node_map[child][parents] = 1
        
    for wire in wires:
        count = 1
        visited = [False for _ in range(n+1)]
        visited[wire[0]] = True
        
        q = deque()
        q.append(wire[0])
        
        while q:
            cur = q.popleft()
            
            for i in range(1, n+1):
                if ((not visited[i]) and (i != wire[1]) and node_map[cur][i] == 1):
                    count+=1
                    q.append(i)
                    visited[i] = True
        
        answer = min(answer, abs(n - 2* count))
        
    return answer

if __name__ == "__main__":
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
    print(solution(4, [[1,2],[2,3],[3,4]]))
    print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))