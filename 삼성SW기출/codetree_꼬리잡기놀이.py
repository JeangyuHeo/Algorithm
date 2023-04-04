from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y, members, flag):
    result = []
    if board[x][y] == 3:
        counts.append(len(members))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny):
            if not visited[nx][ny]:
                if flag:
                    if board[nx][ny] == 2:
                        visited[nx][ny] = True
                        members.append((nx, ny))
                        dfs(nx, ny, members, False)
                else:
                    if board[nx][ny] != 0:
                        visited[nx][ny] = True
                        members.append((nx, ny))
                        dfs(nx, ny, members, flag)

def left_check(x):
    result = []

    for i in range(m):
        for j in range(counts[i]):
            if team[i][j][0] == x:
                num = -1
                if mode[i]:
                    num = counts[i] - j
                else:
                    num = j+1
                result.append([team[i][j][1], num, i])

    if result:
        result.sort(key=lambda l: l[0])
        mode[result[0][2]] = not mode[result[0][2]]

        return result[0][1] ** 2
    return 0

def bottom_check(x):
    result = []

    for i in range(m):
        for j in range(counts[i]):
            if team[i][j][1] == x:
                num = -1
                if mode[i]:
                    num = counts[i] - j
                else:
                    num = j+1
                result.append([team[i][j][0], num, i])
    if result:
        result.sort(key=lambda l: -l[0])
        mode[result[0][2]] = not mode[result[0][2]]

        return result[0][1] ** 2
    return 0

def right_check(x):
    result = []

    for i in range(m):
        for j in range(counts[i]):
            if team[i][j][0] == x:
                num = -1
                if mode[i]:
                    num = counts[i] - j
                else:
                    num = j+1
                result.append([team[i][j][1], num, i])
    
    if result:
        result.sort(key=lambda l: -l[0])
        mode[result[0][2]] = not mode[result[0][2]]

        return result[0][1] ** 2
    return 0

def top_check(x):
    result = []

    for i in range(m):
        for j in range(counts[i]):
            if team[i][j][1] == x:
                num = -1
                if mode[i]:
                    num = counts[i] - j
                else:
                    num = j+1
                result.append([team[i][j][0], num, i])
    
    if result:
        result.sort(key=lambda l: l[0])
        mode[result[0][2]] = not mode[result[0][2]]

        return result[0][1] ** 2
    return 0

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
counts, team = [], []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            visited[i][j] = True
            member = deque([(i,j)])
            dfs(i, j, member, True)
            team.append(member)

mode = [False for _ in range(m)]
answer = 0

for i in range(k):
    for j in range(m):
        if not mode[j]:
            team[j].appendleft(team[j].pop())
        else:
            team[j].append(team[j].popleft())
    
    ty = (i // n) % 4

    if ty == 0:
        answer += left_check(i % n)
    elif ty == 1:
        answer += bottom_check(i % n)
    elif ty == 2:
        answer += right_check(n-1 - (i % n))
    else:
        answer += top_check(n-1 - (i % n))

print(answer)