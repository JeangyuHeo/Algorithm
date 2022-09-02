def solution(n, left, right):
    return [max(i//n, i%n)+1 for i in range(left, right+1)]

if __name__ == "__main__":
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))