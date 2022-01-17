import heapq

def solution(scoville, K):
    answer = 0
    h=[]
    
    for scov in scoville:
        heapq.heappush(h, scov)
    
    while (h[0] < K and len(h) > 1):
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        
        heapq.heappush(h, first + (second * 2))
        
        answer+=1
        
    if h[0] < K:
        return -1
    return answer

print(solution([1,2,3,9,10,12], 7))