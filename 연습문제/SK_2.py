import sys
sys.setrecursionlimit(10**6)

def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = answer[0][-1] = answer[-1][0] = answer[-1][-1] = 1
    
    end = 0
    if n % 2:
        end = n // 2
    else:
        end = n // 2 - 1

    def check_center(x,y):
        if n%2:
            if x==end and y==end:
                return True
        else:
            if any([x == end and y == end, x == end+1 and y == end, x == end and y == end+1, x == end +1 and y == end+1]):
                return True
        return False

    def dfs(matrix, x : int, y : int, count:int, size:int, mode: int, turn:int):
        if check_center(x,y):
            return

        if turn >= 2:
            size -= 1

        if clockwise:
            if mode % 4 == 0:
                for i in range(1, size):
                    answer[x][y+i] = count
                    count+=1
                    if check_center(x, y+i):
                        return

                dfs(matrix, x,y+size-1,count, size-1, mode+1,turn+1)
            elif mode % 4 == 1:
                for i in range(1, size):
                    answer[x+i][y] = count
                    count+=1
                    if check_center(x+i, y):
                        return

                dfs(matrix, x+size-1, y, count, size-1, mode+1,turn+1)
            elif mode % 4 == 2:
                for i in range(1, size):
                    answer[x][y-i] = count
                    count+=1
                    if check_center(x, y-i):
                        return

                dfs(matrix, x,y-size+1, count, size-1, mode+1,turn+1)
            else:
                for i in range(1,size):
                    answer[x-i][y] = count
                    count+=1
                    if check_center(x-i, y):
                        return

                dfs(matrix, x-size+1, y, count, size-1, mode+1,turn+1)
        else:
            if mode % 4 == 0:
                for i in range(1, size):
                    answer[x+i][y] = count
                    count+=1
                    if check_center(x+i, y):
                        return

                dfs(matrix, x+size-1, y, count, size-1, mode+1,turn+1)
            elif mode % 4 == 1:
                for i in range(1, size):
                    answer[x][y+i] = count
                    count+=1
                    if check_center(x, y+i):
                        return

                dfs(matrix, x,y+size-1,count, size-1, mode+1,turn+1)
            elif mode % 4 == 2:
                for i in range(1,size):
                    answer[x-i][y] = count
                    count+=1
                    if check_center(x-i, y):
                        return

                dfs(matrix, x-size+1, y, count, size-1, mode+1,turn+1)
            else:
                for i in range(1, size):
                    answer[x][y-i] = count
                    count+=1
                    if check_center(x, y-i):
                        return
                
                dfs(matrix, x,y-size+1, count, size-1, mode+1,turn+1)

    if clockwise:
        dfs(answer, 0, 0, 2, n-1, 0, 0)
        dfs(answer, 0, n-1, 2, n-1,1, 0)
        dfs(answer, n-1, n-1, 2, n-1,2, 0)
        dfs(answer, n-1, 0, 2, n-1,3, 0)
    else:
        dfs(answer, 0,0,2,n-1,0, 0)
        dfs(answer, n-1, 0, 2, n-1,1, 0)
        dfs(answer, n-1, n-1, 2, n-1,2, 0)
        dfs(answer, 0, n-1, 2, n-1,3, 0)
    
    return answer