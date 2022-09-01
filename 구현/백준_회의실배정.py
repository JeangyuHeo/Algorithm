
if __name__ == "__main__":
    n = int(input())
    answer = 0
    schedule = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
    
    end_time = 0
    for start, end in schedule:
        if start >= end_time:
            end_time = end
            answer+=1
            
    print(answer)