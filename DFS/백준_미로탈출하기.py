import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

move_dict = {'U':0, 'R':1, 'D':2, 'L':3}
    
def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    
    i = move_dict[board[x][y]]
    nx, ny = x+dx[i], y+dy[i]
    
    dp[x][y] = dfs(nx, ny)
        
    return dp[x][y]
        
if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            answer += dfs(r,c)
            
    print(answer)