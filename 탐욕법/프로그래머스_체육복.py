def solution(n, lost, reserve):
    del_reserve = set(reserve)-set(lost) 
    del_lost = set(lost)-set(reserve)
    
    for num in del_reserve:
        if num-1 in del_lost:
            del_lost.remove(num-1)
        elif num+1 in del_lost:
            del_lost.remove(num+1)
    
    return n-len(del_lost)

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(5, [3], [1]))