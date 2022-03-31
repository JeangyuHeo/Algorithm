from copy import deepcopy

def solution(width, height, diagonals):
    def calc_cases(dp,x,y):
        for idx, row in enumerate(range(height-x, -1,-1)):
            if idx == 0:
                start = y
            else:
                start = 0
            for  col in range(start, width+1):
                if row == height:
                    dp[row][col] = dp[row][col-1]
                elif col == 0:
                    dp[row][col] = dp[row+1][col]
                else:
                    dp[row][col] = (dp[row+1][col] + dp[row][col-1])%10000019

        return dp[0][-1]
            
    dp = [[1 for _ in range(width+1)] for _ in range(height+1)]
    answer = 0
    
    calc_cases(dp,0,1)
    
    for x,y in diagonals:
        temp = deepcopy(dp)
        temp[height - x][y-1] += dp[height - x+1][y]
        temp[height - x+1][y] += dp[height - x][y - 1]

        answer += calc_cases(temp, x, y)
        answer %= 10000019
        
    return answer

print(solution(2,2,[[1,1], [2,2]]))
print(solution(51,37,[[17,19]]))