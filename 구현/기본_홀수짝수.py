# 우리가 정해야 하는 것 x
# 홀수 자리는 x 보다 큰 수
# 짝수 자리는 x 보다 작은 수
# index + 1로 수 배정
def solution(nums):
    len_nums = len(nums)
    answer = [-1]
    
    for i in len(len_nums):
        nums[i]
        
    
    return answer

if __name__ == "__main__":
    tc1 = [1,0,0,1,1]
    tc2 = [0,4,0,4,0]
    tc3 = [1,1,1]
    
    print(solution(tc1))
    print(solution(tc2))
    print(solution(tc3))