class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        total = len(isConnected)
        answer = 0
        visited = set()
        
        def dfs(num):
            visited.add(num)
            
            for i in range(total):
                if all([
                    isConnected[num][i] == 1,
                    i not in visited,
                    i != num
                ]):
                    dfs(i)
                    
        for i in range(total):
            if i not in visited:
                dfs(i)
                answer+=1
                
        return answer
        