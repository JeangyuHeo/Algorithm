import heapq

def solution(numbers):
    len_num = len(numbers)
    answer = [-1 for _ in range(len_num)]
    heap = [(numbers[0], 0)]
    
    for i in range(1, len_num):
        while heap and heap[0][0] < numbers[i]:
            _, idx = heapq.heappop(heap)
            answer[idx] = numbers[i]
        heapq.heappush(heap, (numbers[i], i))

    return answer

print(solution([2,3,3,5]))
print(solution([9,1,5,3,6,2]))