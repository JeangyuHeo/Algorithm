import sys

input = sys.stdin.readline

def calc_clock(nums):
    cand = 1e9
    
    for _ in range(4):
        nums.append(nums.pop(0))
        cand = min(cand, arr_to_num(nums))
    
    return cand
    
def arr_to_num(nums):
    return sum([nums[i]*10**(len_nums-i-1) for i in range(len_nums)])

def is_clock(num):
    num_list = list(map(int, str(num)))
    
    if 0 not in num_list and num == calc_clock(num_list):
        return 1
    else:
        return 0

if __name__ == "__main__":
    answer = 1
    clock_nums = list(map(int, input().strip().split()))
    len_nums = len(clock_nums)
                      
    for num in range(1111, calc_clock(clock_nums)):
        answer += is_clock(num)
    
    print(answer)