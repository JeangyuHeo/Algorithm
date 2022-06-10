from copy import deepcopy

def get_combinations():
    result = []
    
    for i in range(m-2):
        for j in range(i+1, m-1):
            for k in range(j+1, m):
                result.append([i,j,k])
                
    return result

def calc_distance(x,y,pos1):
    return abs(n-x) + abs(pos1-y)

def attack_enemy(temp, comb):
    cnt = 0
    total_attacked = []
    
    for pos in comb:
        turn_attacked = []
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:
                    dist = calc_distance(i,j,pos)
                    if dist <= d:
                        turn_attacked.append([dist,i,j])
        
        turn_attacked.sort(key=lambda x: (x[0],x[2]))
        
        if turn_attacked:
            total_attacked.append(turn_attacked[0])
            
    for dist, i, j in total_attacked:
        if temp[i][j] == 1:
            temp[i][j] = 0
            cnt += 1
    return cnt
                   
    
def move_enemy(temp):
    return [[0]*m] + temp[:-1]

def is_exist(tmp_board):
    for i in range(n):
        for j in range(m):
            if tmp_board[i][j] == 1:
                return True
    return False
    
if __name__ == "__main__":
    answer = -1
    n,m,d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    for comb in get_combinations():
        count = 0
        temp = deepcopy(board)
        
        while is_exist(temp):
            count += attack_enemy(temp, comb)
    
            temp = move_enemy(temp)
        
        answer = max(answer, count)
    
    print(answer)