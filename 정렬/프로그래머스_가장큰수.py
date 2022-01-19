def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse = True))))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))