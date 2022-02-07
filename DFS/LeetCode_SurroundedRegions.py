class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        rows = len(board)
        cols = len(board[0])
        
        if any([rows<=2, cols<=2]):
            return
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col]!='O':
                return;
            board[row][col] = '#'
            for m_x, m_y in zip(dx,dy):
                dfs(row+m_x, col+m_y)
                
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][cols-1] == 'O':
                dfs(i, cols-1)
                
        for i in range(cols):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[rows-1][i] == 'O':
                dfs(rows-1, i)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'