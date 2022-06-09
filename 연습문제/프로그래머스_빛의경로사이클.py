dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_way(x, y, d, grid):
    global visited
    
    result = 0
    nx, ny, nd = x,y,d
    visited[x][y][d] = True
    
    while True:
        nx = (nx + dx[nd]) % n
        ny = (ny + dy[nd]) % m
        
        result += 1
        
        if grid[nx][ny] == 'R':
            nd = (nd+1) % 4
        elif grid[nx][ny] == 'L':
            nd = (nd-1) % 4
            
        if visited[nx][ny][nd]:
            if x == nx and y == ny and d == nd:
                return result
            else:
                return 0
        visited[nx][ny][nd]= True
        
    
def solution(grid):
    global visited, n, m
    
    n, m = len(grid), len(grid[0])
    answer = []
    
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            for i in range(4):
                if not visited[x][y][i]:
                    result = check_way(x,y,i,grid)
                    if result != 0:
                        answer.append(result)
    
    return sorted(answer)

if __name__ == "__main__":
    print(solution(["SL","LR"]))
    print(solution(["S"]))
    print(solution(["R","R"]))