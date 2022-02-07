class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        num = len(graph)-1
        
        def dfs(start, path):
            tmp = path[:]
            if start == num:
                answer.append(tmp)
                return
            
            for n in graph[start]:
                tmp.append(n)
                dfs(n, tmp)
                tmp.pop()
        
        dfs(0,[0])
        
        return answer