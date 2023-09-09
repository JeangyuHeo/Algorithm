dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

di = (-1, -1, 1, 1)
dj = (-1, 1, -1, 1)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def grow(x, y):
    cnt = 0

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx, ny):
            if board[nx][ny] > 0 and killer_board[nx][ny] == 0:
                cnt += 1
    board[x][y] = board[x][y] + cnt


def spread_one(x, y):
    cnt, result = 0, []

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx, ny):
            if board[nx][ny] == 0 and killer_board[nx][ny] == 0:
                cnt += 1
                result.append((nx, ny))
        
    return [(a, b, board[x][y] // cnt) for a, b in result]

def spread():
    spreads = []

    for x, y in trees:
        spreads.extend(spread_one(x, y))

    for x, y, size in spreads:
        if (x, y) not in trees and size != 0:
            trees.append((x, y))
        board[x][y] += size

def calc_killer(x, y):
    able = [False for _ in range(4)]
    result = board[x][y]

    for t in range(1, k+1):
        for i in range(4):
            if not able[i]:
                nx, ny = x+(di[i]*t), y+(dj[i]*t)
                if in_range(nx, ny):
                    if board[nx][ny] > 0:
                        result += board[nx][ny]
                    else:
                        able[i] = True
    
    return result

def set_killer(x, y):
    able = [False for _ in range(4)]
    board[x][y] = 0
    tree_remove(x,y)
    killer_board[x][y] = c

    for t in range(1, k+1):
        for i in range(4):
            if not able[i]:
                nx, ny = x+(di[i]*t), y+(dj[i]*t)
                if in_range(nx, ny):
                    if board[nx][ny] > 0:
                        tree_remove(nx, ny)
                        board[nx][ny] = 0
                        killer_board[nx][ny] = c
                    else:
                        killer_board[nx][ny] = c
                        able[i] = True
def tree_remove(x, y):
    for i in range(len(trees)):
        if trees[i] == (x, y):
            trees.pop(i)
            break
    
def killing():
    max_val, max_idx = -1, ()

    for i in range(len(trees)):
        x, y = trees[i]
        val = calc_killer(x, y)

        if val > max_val:
            max_val = val
            max_idx = (x, y)
        
        elif val == max_val:
            max_idx = min(max_idx, (x, y))

    if max_idx:
        set_killer(*max_idx)

    return max(max_val, 0)


def find_tree():
    result = []

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                result.append((i, j))
    return result

def decrease_killer():
    for i in range(n):
        for j in range(n):
            if killer_board[i][j] > 0:
                killer_board[i][j] -= 1

        
if __name__ == "__main__":
    n, m, k, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    killer_board = [[0 for _ in range(n)] for _ in range(n)]
    trees = find_tree()
    answer = 0
    
    for _ in range(m):
        for x, y in trees:
            grow(x, y)
        spread()
        decrease_killer()
        answer += killing()
        
print(answer)