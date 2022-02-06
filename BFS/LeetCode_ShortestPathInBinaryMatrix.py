class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        
        if rows == 0 and cols == 0:
            return 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        
        answer = 1
        
        q = [(0,0)]
        
        visited = set()
        visited.add((0,0))
        
        while q:
            for _ in range(len(q)):
                x, y = q.pop(0)
                for m_x, m_y in zip(dx, dy):
                    if 0 <= x+m_x <= rows and 0 <= y+m_y <= cols and grid[x+m_x][y+m_y] == 0 and (x+m_x, y+m_y) not in visited:
                        visited.add((x+m_x, y+m_y))
                        q.append((x+m_x, y+m_y))
                        if x+m_x == rows and y+m_y == cols:
                            return answer + 1
            answer+=1
        
        return -1