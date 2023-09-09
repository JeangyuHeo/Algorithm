def solution(number, limit, power):
    answer = []
    
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                if j ** 2 == i:
                    cnt += 1
                else:
                    cnt += 2
                
        answer.append(cnt)

    return sum([num if num <= limit else power for num in answer])

if __name__ == "__main__":
    print(solution(5, 3, 2), 10)
    print(solution(10, 3, 2), 21)