import sys

input = sys.stdin.readline

def dfs(strength):
    if strength < 500:
        return
    
    if False not in visited:
        global answer
        answer += 1
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(strength+kits[i]-k)
            visited[i] = False

if __name__ == "__main__":
    answer = 0
    n, k = map(int, input().strip().split())
    kits = list(map(int, input().strip().split()))
    visited = [False for _ in range(n)]
    
    dfs(500)
    
    print(answer)