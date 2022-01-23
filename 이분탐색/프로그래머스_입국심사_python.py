def solution(n, times):
    answer = 1e9
    
    min_time = 0
    max_time = max(times) * n
    
    while min_time <= max_time:
        avg_time = (min_time + max_time) // 2
        cnt=0
        
        for time in times:
            cnt += avg_time // time
            
        if n > cnt:
            min_time = avg_time+1
        else:
            max_time = avg_time-1
            answer = avg_time

    return answer

print(solution(6,[7,10]))