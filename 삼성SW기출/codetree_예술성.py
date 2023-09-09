from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def make_group():
    global group_map
    visited = [[False for _ in range(n)] for _ in range(n)]
    group_cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt = 1
                visited[i][j] = True
                group_map[i][j] = group_cnt
                
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()

                    for idx in range(4):
                        nx, ny = x+dx[idx], y+dy[idx]
                        if in_range(nx, ny):
                            if color_map[nx][ny] == color_map[i][j]:
                                if not visited[nx][ny]:
                                    q.append((nx, ny))
                                    cnt += 1
                                    visited[nx][ny] = True
                                    group_map[nx][ny] = group_cnt
                group_num[group_cnt] = cnt
                group_cnt += 1

    return group_cnt

def calc_point():
    result = 0

    for r in range(n):
        for c in range(n):
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if in_range(nr, nc):
                    if group_map[r][c] != group_map[nr][nc]:
                        result += (group_num[group_map[r][c]] + group_num[group_map[nr][nc]]) * color_map[r][c] * color_map[nr][nc]
        
    return result // 2

def rotate_cross():
    half = n // 2 

    for i in range(1, half+1):
        color_map[half-i][half], color_map[half][half-i], color_map[half+i][half], color_map[half][half+i] =\
        color_map[half][half+i], color_map[half-i][half], color_map[half][half-i], color_map[half+i][half]

def rotate_small_square(s_x, e_x, s_y, e_y):
    size = e_x - s_x + 1
    arr = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            arr[j][size-1-i] = color_map[s_x+i][s_y+j]
    
    for i in range(size):
        for j in range(size):
            color_map[s_x+i][s_y+j] = arr[i][j]

def rotate_square():
    rotate_small_square(0, mid - 1, 0 , mid - 1)
    rotate_small_square(mid + 1, n - 1, 0 , mid - 1)
    rotate_small_square(0, mid - 1, mid + 1 , n - 1)
    rotate_small_square(mid + 1, n - 1, mid + 1 , n - 1)


if __name__ == "__main__":
    n = int(input())
    color_map = [list(map(int, input().split())) for _ in range(n)]
    point = 0
    mid = n // 2

    for x in range(4):
        group_map = [[0 for _ in range(n)] for _ in range(n)]
        group_num = {}

        group_cnt = make_group()
        point += calc_point()

        if x == 3:
            break

        rotate_cross()
        rotate_square()

print(point)