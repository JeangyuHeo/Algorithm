

if __name__ == "__main__":
    dx = (-1, 0, 0, 1)
    dy = (0, 1, -1, 0)

    answer = 0
    n = int(input())
    class_room = [[0 for _ in range(n)] for _ in range(n)]
    pref = [list(map(int, input().split())) for _ in range(n*n)]

    for i in range(n*n):
        student = pref[i]

        tmp = []
        for j in range(n):
            for k in range(n):
                if class_room[j][k] == 0:
                    like = 0
                    blank = 0

                    for l in range(4):
                        nx = j + dx[l]
                        ny = k + dy[l]
                        if 0<=nx<n and 0<=ny<n:
                            if class_room[nx][ny] in student[1:]:
                                like+=1
                            if class_room[nx][ny] == 0:
                                blank+=1
                        
                    tmp.append([like, blank, j,k])
        tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        class_room[tmp[0][2]][tmp[0][3]] = student[0]

    pref.sort()

    for i in range(n):
        for j in range(n):
            res = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if class_room[nx][ny] in pref[class_room[i][j]-1]:
                        res += 1
            if res != 0:
                answer += 10 ** (res-1)

        print(answer)