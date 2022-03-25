import sys

input = sys.stdin.readline
NUM_BLOCK = 4

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def dfs(x, y, sum, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, sum)
        return

    if sum + max_val * (4-cnt) < answer:
        return

    for i in range(NUM_BLOCK):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < m:
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                if cnt == 2:
                    dfs(x, y, sum + board[next_x][next_y], cnt + 1)
                dfs(next_x, next_y, sum + board[next_x][next_y], cnt + 1)
                visited[next_x][next_y] = False


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = 0
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split(" "))))

    max_val = max(map(max, board))

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, board[i][j], 1)
            visited[i][j] = False

    print(answer)