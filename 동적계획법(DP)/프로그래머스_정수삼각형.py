def solution(triangle):
    height = len(triangle)
    
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif i==j:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
    return max(triangle[-1])