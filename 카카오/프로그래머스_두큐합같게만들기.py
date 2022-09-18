from collections import deque

def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    total = sum_q1 + sum_q2
    len_q = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = -2
    
    for i in range(3 * len_q):
        if sum_q1 == sum_q2:
            return i
        elif sum_q1 < sum_q2:
            sum_q2 -= queue2[0]
            sum_q1 += queue2[0]
            queue1.append(queue2.popleft())
        else:
            sum_q1 -= queue1[0]
            sum_q2 += queue1[0]
            queue2.append(queue1.popleft())
        
    return -1

if __name__ == "__main__":
    print(solution([3,2,7,2], [4,6,5,1]))
    print(solution([1,2,1,2], [1,10,1,2]))
    print(solution([1,1], [1,5]))