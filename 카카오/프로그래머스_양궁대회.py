from collections import deque
from itertools import combinations_with_replacement, combinations

def solution(n, info):
    answer = [-1]
    max_gap = -1
    
    for comb in combinations_with_replacement(range(11), n):
        lion_list = [0 for _ in range(11)]
        lion, apeach = 0, 0
        
        for i in comb:
            lion_list[10-i] += 1
            
        for i in range(11):
            if (info[i], lion_list[i]) == (0,0):
                continue
            elif info[i] >= lion_list[i]:
                apeach += 10 - i
            else:
                lion += 10 - i
        if lion > apeach:
            if lion - apeach > max_gap:
                max_gap = lion - apeach
                answer = lion_list
    return answer

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap 
                    res.clear()
                res.append(arrow)
        
        elif sum(arrow) > n:
            continue
        
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]

if __name__ == "__main__":
    print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
    print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
    print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
    print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))