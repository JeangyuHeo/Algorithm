from collections import defaultdict

def calc_total(pick):
    total = 0
    
    for h_r, h_c in house_list:
        min_dist = 1e9
        for i in pick:
            min_dist = min(min_dist, abs(chicken_list[i][0]- h_r) + abs(chicken_list[i][1] - h_c))
            
        total += min_dist
        
    return total
    
    
def dfs(idx, pick):
    global answer
    if len(pick) == M:
        answer = min(answer, calc_total(pick))
        return
    if idx == len(chicken_list):
        return
    else:
        dfs(idx+1, pick + [idx])
        dfs(idx+1, pick)
    
if __name__ == "__main__":
    answer = 1e9
    N, M = map(int, input().split(" "))
    board = [list(map(int, input().split(' '))) for _ in range(N)]
    chicken_list = []
    house_list = []
    
    # 0: 빈킨, 1: 집, 2: 치킨집
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                house_list.append((i,j))
            elif board[i][j] == 2:
                chicken_list.append((i,j))
    
    dfs(0,[])
    
    print(answer)