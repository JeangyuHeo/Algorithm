import heapq

#constants
RED = 0
GREEN = 1
BLUE = 2

def find_minimum(cards, color):
    h = []
    
    for idx, nums in enumerate(cards):
        heapq.heappush(h, (nums[color], idx))
    
    print(h)
        
def solution(cards):
    answer = 0
        
    
    return answer

#test case
cards1 = [[10, 5, 15], [5, 15, 10], [10, 11, 9]] # 21
cards2 = [[10, 5, 15], [8, 9, 13], [10, 10, 10]] # 23
cards3 = [[ 8,11, 11], [6, 15, 9], [14, 2, 14], [8, 20, 2]] # 22
cards4 = [[ 8,11, 11], [10, 7, 13], [15, 10, 5], [7, 17, 6]] # 28
cards5 = [[0, 0, 30], [30, 0, 0]] # 0

print(find_minimum(cards1, RED))
print(find_minimum(cards2, RED))
print(find_minimum(cards3, RED))
print(find_minimum(cards4, RED))
print(find_minimum(cards5, RED))


print(solution(cards1))
print(solution(cards2))
print(solution(cards3))
print(solution(cards4))
print(solution(cards5))