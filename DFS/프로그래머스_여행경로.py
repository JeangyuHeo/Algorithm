def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def DFS(start,cnt, result):
        result.append(start)
        
        nonlocal answer
        
        if cnt == len(tickets):
            if len(answer) == 0:
                answer.extend(result)
            return
        
        for idx, ticket in enumerate(tickets):
            if all([ticket[0] == start, not visited[idx]]):
                visited[idx] = True
                DFS(ticket[1],cnt+1,result)
                visited[idx] = False
        
        result.pop()
    
    tickets = sorted(tickets, key = lambda x: (x[1],x[0]))
    
    DFS("ICN",0, [])
    
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))