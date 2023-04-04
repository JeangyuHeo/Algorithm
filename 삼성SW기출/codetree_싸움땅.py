dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def in_range(r, c):
    return 0<=r<n and 0<=c<n

def change_weapon(i, r, c):
    max_damage = max(board[r][c])
    if max_damage > weapon[i]:
        board[r][c].remove(max_damage)
        if weapon[i] != 0:
            board[r][c].append(weapon[i])
        weapon[i] = max_damage
    
    if not board[r][c]:
        board[r][c].append(0)

def fight(i, r, c):
    j = -1
    for k in range(m):
        if pos[k] == [r,c]and i != k:
            j = k

    total_a = weapon[i] + stats[i]
    total_b = weapon[j] + stats[j]

    diff = abs(total_a - total_b)
    winner, loser = -1, -1

    if (total_a, stats[i]) > (total_b, stats[j]):
        winner = i
        loser = j
    else:
        winner = j
        loser = i

    score[winner] += diff

    board[r][c].append(weapon[winner])
    board[r][c].append(weapon[loser])
    cur_weapons = sorted(board[r][c], reverse=True)
    weapon[loser] = 0

    nr, nc = r+dx[dirs[loser]] , c+dy[dirs[loser]]

    if [nr, nc] in pos or not in_range(nr, nc):
        for _ in range(4):
            dirs[loser] = (dirs[loser] + 1) % 4
            nr, nc = r+dx[dirs[loser]], c+dy[dirs[loser]]

            if in_range(nr, nc) and [nr,nc] not in pos:
                break
    
    pos[loser] = [nr, nc]
    change_weapon(loser, nr, nc)
    
    weapon[winner] = cur_weapons[0]
    board[r][c] = cur_weapons[1:]
    

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board = [list(map(lambda x: [x], row)) for row in board]
players = [list(map(int, input().split())) for _ in range(m)]
weapon = [0 for _ in range(m)]

pos, dirs, stats = [], [], []
score = [0 for _ in range(m)]

for x, y, d, s in players:
    pos.append([x-1,y-1])
    dirs.append(d)
    stats.append(s)


for _ in range(k):
    for i in range(m):
        x, y = pos[i]
        nx, ny = x + dx[dirs[i]], y + dy[dirs[i]]

        if not in_range(nx, ny):
            dirs[i] = (dirs[i] + 2) % 4
            nx, ny = x + dx[dirs[i]], y + dy[dirs[i]]

        if [nx, ny] in pos:
            pos[i] = [nx, ny]
            fight(i, nx, ny)
        else:
            pos[i] = [nx, ny]
            change_weapon(i, nx, ny)
        
print(*score)