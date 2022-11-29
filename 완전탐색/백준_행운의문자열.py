import sys
from collections import Counter

input = sys.stdin.readline

def dfs(prev, l):
    global answer
    if l == len_s:
        answer += 1
        return
    
    for key in s_dict.keys():
        if key != prev and s_dict[key] != 0:
            s_dict[key] -= 1
            dfs(key, l+1)
            s_dict[key] += 1
    
if __name__ == "__main__":
    answer = 0
    s = list(input().strip())
    len_s = len(s)
    s_dict = Counter(s)
    
    dfs('', 0)
    
    print(answer)