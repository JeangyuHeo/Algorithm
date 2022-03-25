from collections import defaultdict

def solution(n, edges):
    answer = 0
    length = len(edges)
    dic = defaultdict(int)

    for start, end in edges:
        dic[start] += 1
    count = 0
    for key, val in dic.items():
        if val > 1:
            count+=1
        
    return length**2 if count >=2 else length**2 - 1