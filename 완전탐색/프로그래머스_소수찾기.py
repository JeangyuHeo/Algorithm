import copy

def solution(numbers):
    answer = 0
    d=[0]*9999999
    n=[0]*10
    
    numbers = "".join(sorted(numbers, reverse=True))
    
    max_num = int(numbers)
    
    for i in range(2, max_num+1):
        if not d[i]:
            j=2
            while i*j<=max_num:
                d[i*j]=1
                j+=1
                
    for num in numbers:
        n[int(num)]+=1
    
    for i in range(2, max_num+1):
        if d[i]: 
            continue
            
        tmp = str(i)
        tmp_n = copy.deepcopy(n)
        
        for idx, num in enumerate(tmp):
            if tmp_n[int(num)] <= 0:
                break
            tmp_n[int(num)]-=1
            if idx == len(tmp)-1:
                
                answer+=1
        
    
    return answer