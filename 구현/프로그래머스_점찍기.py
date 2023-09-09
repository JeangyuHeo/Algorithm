def solution(k, d):
    return sum([x//k + 1 for x in [int((d**2 - i**2)**(1/2)) for i in range(0, d+1, k)]])

print(solution(2, 4))
print(solution(1, 5))