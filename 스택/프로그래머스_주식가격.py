def solution(prices):
    length = len(prices)
    answer = [0] * length
    
    for i in range(length):
        for j in range(i+1, length):
            answer[i]+=1
            if prices[i] > prices[j]:
                break
                
    
    return answer

print(solution([1,2,3,2,3]))