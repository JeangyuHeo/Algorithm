import sys

input = sys.stdin.readline

dx = (1, 0)
dy = (0, 1)


def dfs(x, y, express, is_oper):
    if (x,y) == (n-1, n-1):
        global max_ans, min_ans
        total_score = eval(express)
        max_ans = max(max_ans, total_score)
        min_ans = min(min_ans, total_score)
        return
    
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if is_oper:
                    dfs(nx, ny, express+board[nx][ny], False)
                else:
                    dfs(nx,ny, "("+express+board[nx][ny]+")", True)
                visited[nx][ny] = False
                

if __name__ == "__main__":
    max_ans, min_ans = -1e9, 1e9
    n = int(input())
    board = [list(input().strip().split()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    
    dfs(0,0,board[0][0], True)
    print(max_ans, min_ans)