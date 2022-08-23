
    
def calc_bomb():
    r = m//2
    start, end = r, n-r
    
    for i in range(start,end):
        for j in range(start, end):
            answer[i][j] = univ[i-r][j-r]
            if i -r - 1 >= 0:
                answer[i][j] -= univ[i-r-1][j-r]
            if j-r-1 >= 0:
                answer[i][j] -= univ[i-r][j-r-1]
            if i-r-1 >= 0 and j-r-1 >=0:
                answer[i][j] += univ[i-r-1][j-r-1]
            if i-m >= 0:
                answer[i][j] += answer[i-m][j]
            if j-m >= 0:
                answer[i][j] += answer[i][j-m]
            if i-m >= 0 and j-m >= 0:
                answer[i][j] -= answer[i-m][j-m]
                
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    univ = []
    for _ in range(n):
        input_list = list(map(int, input().split()))
        univ.append(list(map(lambda x: x*-1, input_list)))
            
    answer = [[0 for _ in range(n)] for _ in range(n)]

    calc_bomb()

    for r in answer:
        print(*r)