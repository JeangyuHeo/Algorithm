def solution(number):
    answer = 0
    len_num = len(number)
    
    for i in range(len_num-2):
        for j in range(i+1, len_num-1):
            for k in range(j+1, len_num):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

if __name__ == "__main__":
    print(solution([-2, 3, 0, 2, -5]), 2)
    print(solution([-3, -2, -1, 0, 1, 2, 3]), 5)
    print(solution([-1, 1, -1, 1]), 0)