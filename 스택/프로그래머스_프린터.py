def solution(priorities, location):
    answer = 1
    q=[]
    for idx, priority in enumerate(priorities):
        q.append((priority, idx))

    while q:
        val = q.pop(0)
        
        if q and val[0] < max(q)[0]:
            q.append(val)
        else:
            if val[1] == location:
                return answer
            answer+=1
        
    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))