import sys
from collections import deque

input = sys.stdin.readline

def dfs(pos, money):
    global answer
    if info[pos][0] == 'L':
        ref = int(info[pos][1])
        if money < ref:
            money = ref
        
    elif info[pos][0] == 'T':
        troll = int(info[pos][1])
        if money < troll:
            return
        money -= troll
    
    if pos == n:
        answer = 'Yes'
        return

    visited[pos] = True
    
    for next in map(int, info[pos][2:]):
        if not visited[next]:
            dfs(next, money)
            
    visited[pos] = False

if __name__ == "__main__":
    while True:
        n = int(input())
        
        if not n:
            break
        answer = 'No'
        info = [0]+[input().split()[:-1] for _ in range(n)]
        visited = [False for _ in range(n+1)]
        
        dfs(1,0)
        
        print(answer)