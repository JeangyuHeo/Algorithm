import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dp = [[[1e9 for _ in range(max_hp+1)] for _ in range(max_hp+1)] for _ in range(max_hp+1)]
    q = deque([hp])
    dp[hp[0]][hp[1]][hp[2]] = 0
    
    while q:
        scv1, scv2, scv3 = q.popleft()

        if all([scv1<=0, scv2<=0, scv3<=0]):
            print(dp[scv1][scv2][scv3])
            break
        
        for i in range(6):
            tmp = []
            nscv1 = scv1-pers[i][0]
            nscv2 = scv2-pers[i][1]
            nscv3 = scv3-pers[i][2]
            
            nscv1 = nscv1 if nscv1>=0 else 0
            nscv2 = nscv2 if nscv2>=0 else 0
            nscv3 = nscv3 if nscv3>=0 else 0
            
            if dp[nscv1][nscv2][nscv3] == 1e9 or dp[nscv1][nscv2][nscv3] > dp[scv1][scv2][scv3] + 1:
                dp[nscv1][nscv2][nscv3] = dp[scv1][scv2][scv3] + 1
                q.append([nscv1, nscv2, nscv3])
        
if __name__ == "__main__":
    pers = (
        (9, 3, 1),
        (9, 1, 3),
        (3, 9, 1),
        (3, 1, 9),
        (1, 3, 9),
        (1, 9, 3)
    )
    
    answer = 0
    n = int(input())
    hp = list(map(int, input().split()))
    if len(hp) < 3:
        for _ in range(3-len(hp)):
            hp.append(0)
    max_hp = max(hp)
    bfs()