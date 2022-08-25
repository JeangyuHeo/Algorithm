dx = [0, 1, 0, 1, 2, 1]
dy = [1, 0, 2, 1, 0, -1]

def check_path(place, mode, nx, ny):
    if mode == 2:
        if place[nx][ny-1] in ('O', 'P'):
            return False
    elif mode == 3:
        if place[nx][ny-1] in ('O', 'P') or place[nx-1][ny] in ('O', 'P'):
            return False
    elif mode == 4:
        if place[nx-1][ny] in ('O', 'P'):
            return False
    elif mode == 5:
        if place[nx-1][ny] in ('O', 'P') or place[nx][ny+1] in ('O', 'P'):
            return False
    elif mode in (0,1):
        return False
    
    return True

def check_room(place):
    for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    for i in range(6):
                        nr, nc = r+dx[i], c+dy[i]
                        if 0<=nr<5 and 0<=nc<5:
                            if place[nr][nc] == 'P':
                                if not check_path(place,i,nr,nc):
                                    return 0
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check_room(place))
                          
    return answer

if __name__ == "__main__":
    places =[
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
    
    print(solution(places))