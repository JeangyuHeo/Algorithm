if __name__ == "__main__":
    n,m = map(int, input().split())
    time = []
    answer = 1e9
    
    for _ in range(n):
        time.append(int(input()))
    
    min_time = 0
    max_time = max(time) * m
    
    while min_time <= max_time:
        
        mid = (min_time+max_time) // 2
        result = 0
        
        for t in time:
            result += mid // t
        
        if m > result:
            min_time = mid + 1
        else:
            max_time = mid - 1
            answer = mid
            
    print(answer)