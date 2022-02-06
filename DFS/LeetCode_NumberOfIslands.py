class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[0 for col in range(cols)] for row in range(rows)]
        
        def dfs(row, col):
            if grid[row][col] == 0:
                return
            
            nonlocal visited
            visited[row][col] = 1
            
            for i in range(4):
                if all([-1<row+dx[i]<rows, -1<col+dy[i]<cols]):
                    if all([visited[row+dx[i]][col+dy[i]] == 0, grid[row+dx[i]][col+dy[i]] == "1"]):
                        dfs(row+dx[i], col+dy[i])
        
        for row in range(rows):
            for col in range(cols):
                if all([visited[row][col] == 0, grid[row][col] == "1"]):
                    dfs(row,col)
                    answer+=1
        
        return answer