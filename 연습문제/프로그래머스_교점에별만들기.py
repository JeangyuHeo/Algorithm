def solution(line):
    min_x, min_y, max_x, max_y = 1e10, 1e10, -1e10, -1e10
    cross, answer = [], []
    
    num_line = len(line)
    
    for i in range(num_line-1):
        for j in range(i+1, num_line):
            a,b,e = line[i]
            c,d,f = line[j]
            
            deno = a*d - b*c
            
            if deno == 0:
                continue
            
            x_numer = b*f - e*d
            y_numer = e*c - a*f
            
            if x_numer % deno or y_numer % deno:
                continue
                
            x = x_numer // deno
            y = y_numer // deno
            
            min_x = min(x, min_x)
            min_y = min(y, min_y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            
            if (x,y) not in cross:
                cross.append((x,y))
    
    x_size = int(max_x - min_x) + 1
    y_size = int(max_y - min_y) + 1
    
    answer = [["." for _ in range(x_size)] for _ in range(y_size)]
    
    for x,y in cross:
        answer[y_size-(y-min_y)-1][x - min_x] = "*"

    return ["".join(row) for row in answer]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))