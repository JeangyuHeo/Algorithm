from collections import deque

def bfs(x,y):
    visited=[[False for _ in range(m)] for _ in range(n)]
    q = deque()

    q.append((x,y,0))
    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()

        if board[x][y] == 1:
            return cnt
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt+1))

    return -1

if __name__ == "__main__":
    dx = (-1, -1, -1, 0, 1, 1, 1, 0)
    dy = (-1, 0, 1, 1, 1, 0, -1, -1)

    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    answer = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                answer = max(answer, bfs(i, j))

    print(answer)