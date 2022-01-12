from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    
    for cloth in clothes:
        dic[cloth[1]]+=1
    
    for val in dic.values():
        answer *= val+1
        
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))