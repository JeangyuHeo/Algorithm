from collections import defaultdict

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x,y, idx, string):
    if idx == 5:
        return
    
    hash_str[string] += 1
    
    for i in range(8):
        nx, ny = (x+dx[i]) % n, (y+dy[i]) % m
        if nx < 0:
            nx = n+nx
        if ny < 0:
            ny = m+ny
        dfs(nx, ny, idx+1, string+board[nx][ny])

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [input() for _ in range(n)]
    favorites = [input() for _ in range(k)]
    hash_str = defaultdict(int)
    
    for r in range(n):
        for c in range(m):
            dfs(r, c, 0, board[r][c])
    
    for favorite in favorites:
        print(hash_str[favorite])