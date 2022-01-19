def solution(land):
    answer = 0
    length = len(land)
    
    for i in range(1, length):
        for j in range(4):
            cur = land[i][j]
            for k in range(4):
                if j != k:
                    land[i][j] = max(land[i][j], land[i-1][k] + cur)

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))