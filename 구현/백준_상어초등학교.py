
if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    
    answer = 0
    n = int(input())
    pref = [list(map(int, input().split())) for _ in range(n**2)]
    pref_dict ={}
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n**2):
        tmp = []
        cur = pref[i]
        pref_dict[cur[0]] = cur[1:]
        
        for x in range(n):
            for y in range(n):
                like, empty = 0, 0
                
                if board[x][y] == 0:
                    for dir in range(4):
                        nx, ny = x+dx[dir], y+dy[dir]
                        if 0<=nx<n and 0<=ny<n:
                            if board[nx][ny] == 0:
                                empty+=1
                            elif board[nx][ny] in cur[1:]:
                                like+=1
                    tmp.append([like, empty, x, y])
                
        tmp.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
        
        board[tmp[0][2]][tmp[0][3]] = cur[0]

    for x in range(n):
        for y in range(n):
            cnt = 0
            for dir in range(4):
                nx, ny = x+dx[dir], y+dy[dir]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] in pref_dict[board[x][y]]:
                        cnt += 1
            
            if cnt != 0:
                answer += 10 ** (cnt-1)
                
    print(answer)