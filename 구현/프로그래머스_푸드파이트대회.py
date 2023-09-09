def solution(food):
    s, e = '', ''
    
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            s += str(i)
            e = str(i) + e
    
    return s + '0' + e

if __name__ == "__main__":
    print(solution([1, 3, 4, 6]))
    print(solution([1, 7, 1, 2]))