from collections import deque

def solution(brown, yellow):
    answer = []
    q = deque([])
    area = brown + yellow
    
    q.append(3)
    
    while True:
        height = q.popleft()
        
        if area % height == 0:
            width = area / height
            if yellow == (width - 2) * (height - 2):
                answer.append(area / height)
                answer.append(height)
                break
        
        q.append(height+1)
    
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))