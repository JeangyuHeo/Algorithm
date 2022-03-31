def check_mid(mid, x, y):
    if x == mid and y==mid:
        return True
    return False
def calc_wind(answer, n, clockwise):
    size = n - 1
    x, y, count, num = 0, 0, 0, 1
    mid = n//2
        
    if clockwise:
        while (x!=mid or y!=mid) and size > 0:
            if count >= 2:
                size -= 1
                
            if count % 4 == 0:
                for i in range(size):
                    if i!=0 or count!=0:
                        y += 1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num += 1
            elif count % 4 == 1:
                for i in range(size):
                    x += 1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num += 1
            elif count % 4 == 2:
                for i in range(size):
                    y-= 1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num+=1
            else:
                for i in range(size):
                    x-=1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num+=1
            size-=2
            count+=1
            
    else:
        while (x!=mid or y!=mid) and size > 0:
            if count % 4 == 0:
                for i in range(size):
                    if i!=0 or count!=0:
                        x += 1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num += 1
            elif count % 4 == 1:
                for i in range(size):
                    y += 1
                    answer[x][y] = num
                    if check_mid(mid, x,y):
                        break
                    num += 1
            elif count % 4 == 2:
                for i in range(size):
                    x-=1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num+=1
            else:
                for i in range(size):
                    y-= 1
                    if check_mid(mid, x,y):
                        break
                    answer[x][y] = num
                    num+=1
            size-=2
            count+=1
            
    answer[mid][mid] = num
        
def rotate_matrix(answer, n):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            temp[i][j] = answer[n-j-1][i]
    
    return temp
            
def solution(n:int, clockwise:bool):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    
    for _ in range(4):
        calc_wind(answer, n, clockwise)
        answer = rotate_matrix(answer, n)
    
    return answer

print(solution(5, True))
print(solution(6, False))
print(solution(9, False))