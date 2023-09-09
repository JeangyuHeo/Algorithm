dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

move_dict = {"N":0, "E": 1, "S":2, "W":3}

def solution(park, routes):
    n, m = len(park), len(park[0])
    start = 0
    
    for i in range(n):
        if "S" in park[i]:
            for j in range(m):
                if park[i][j] == "S":
                    start = (i, j)
        if start:
            break

    for route in routes:
        op, num = route[0], int(route[2])
        cur_dx, cur_dy = dx[move_dict[op]], dy[move_dict[op]]
        nx, ny = start[0] + (cur_dx * num), start[1] + (cur_dy * num)
        
        if 0<=nx<n and 0<=ny<m:
            flag = True
            for i in range(1, num+1):
                if park[start[0] + cur_dx*i][start[1] + cur_dy*i] == 'X':
                    flag = False
                    break
                    
            if flag:
                start = [nx, ny]
                
    return start

if __name__ == "__main__":
    print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]), [2,1])
    print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]), [0,1])
    print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]), [0,0])