import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
    max_answer = -1e9
    min_answer = 1e9
    
    n = int(input())
    nums = list(map(int, input().split(" ")))
    num_operators = list(map(int, input().split(" ")))
    operators = []
    for idx, num in enumerate(num_operators):
        for _ in range(num):
            operators.append(idx)
            
    pers = list(set(permutations(operators, n-1)))
    
    for per in pers:
        result = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                result=num
            else:
                if per[idx-1] == 0:
                    result += num
                elif per[idx-1] == 1:
                    result -= num
                elif per[idx-1] == 2:
                    result *= num
                elif per[idx-1] == 3:
                    if result < 0:
                        temp = abs(result)
                        temp //= num
                        result = -temp
                    else:
                        result //= num
                    
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)

    print(max_answer)
    print(min_answer)