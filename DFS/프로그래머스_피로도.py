def dfs(dungeons, k, cnt):
    global answer
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if not visited[i]:
            if k >= dungeons[i][0]:
                visited[i]=True
                dfs(dungeons, k-dungeons[i][1], cnt+1)
                visited[i]=False
    

def solution(k, dungeons):
    global answer, visited
    
    answer = -1
    
    visited = [False for _ in range(len(dungeons))]
    
    dfs(dungeons, k, 0)
    
    return answer

if __name__ =="__main__":
    print(solution(80,[[80,20],[50,40],[30,10]]))