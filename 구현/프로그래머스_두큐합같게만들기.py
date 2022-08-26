from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    for cnt in range(len(queue1) * 3):
        if sum1 == sum2:
            return cnt
        
        elif sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
            
        else:
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
            
    return -1

if __name__ == "__main__":
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
    print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
    print(solution([1, 1], [1, 5]))