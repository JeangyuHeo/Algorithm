def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)  
        for j in range(2, int(i**0.5)+1):
            if i%j == 0 and i//j <= 10000000:
                k = i//j  
                break
        answer.append(k)
    
    return answer

if __name__ == "__main__":
    print(solution(1, 10))