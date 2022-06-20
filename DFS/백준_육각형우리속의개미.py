
dx = [-1,-1,1,1,1,-1]
dy = [0,1,1,0,-1,-1]

next_way = [
    [1,5], 
    [0,2], 
    [1,3], 
    [2,4], 
    [3,5], 
    [0,4]
]

def dfs(x, y, cnt, dir):
    #print(x,y)
    if cnt == n:
        if visited[x][y]:
            global answer
            answer += 1
        return
    if visited[x][y]:
        return
    
    visited[x][y] = True
    
    for i in next_way[dir]:
        nx = x + dx[i]
        ny = y + dy[i]

        dfs(nx, ny, cnt+1, i)
    
    visited[x][y] = False
            
    
if __name__ == "__main__":
    n = int(input())
    answer = 0
    visited = [[False for _ in range(100)] for _ in range(100)]
    
    visited[51][50] = True
    
    dfs(50,50,0,0)
    
    print(answer)