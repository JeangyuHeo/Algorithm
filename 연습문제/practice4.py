def get_median(arr):
    return sorted(arr)[len(arr)//2]

def solution(matrix):
    answer=0
    col_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    row_median = set(get_median(row) for row in matrix)
    col_median = set(get_median(col) for col in col_matrix)
    
    return len(row_median - (row_median-col_median))
    

case1 = [
    [1,19,20,8,25],
    [21,4,3,17,24],
    [12,5,6,16,15],
    [11,18,10,9,23],
    [7,13,14,22,2]
]

case2 = [
    [4,2,9],
    [1,3,5],
    [6,8,7]
]

print(solution(case1))
print(solution(case2))