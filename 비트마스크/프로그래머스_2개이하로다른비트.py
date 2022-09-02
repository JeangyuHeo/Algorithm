def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            bit_mask = 1
            for i in range(0, num+1):
                if (num & (bit_mask << i)) == 0:
                    answer.append(num + (bit_mask << (i-1)))
                    break
    
    return answer

if __name__ == "__main__":
    print(solution([2,7]))