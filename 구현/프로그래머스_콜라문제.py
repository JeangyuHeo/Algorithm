def solution(a, b, n):
    answer = 0
    
    cola = (n // a) * b
    remain = n % a
    
    while cola > 0:
        answer += cola
        cola += remain
        remain = cola % a
        cola = (cola // a) * b
        
    return answer

if __name__ == "__main__":
    print(solution(2, 1, 20), 19)
    print(solution(3, 1, 20), 9)