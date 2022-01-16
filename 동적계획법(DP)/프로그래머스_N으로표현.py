def solution(N, number):
    answer = [[]]
    
    for i in range(1, 9):
        temp = []
        
        for j in range(1, i):
            for k in answer[j]:
                for l in answer[i-j]:
                    temp.append(k+l)
                    if k-l >= 0:
                        temp.append(k-l)
                    temp.append(k*l)
                    
                    if l != 0 and k != 0:
                        temp.append(k // l)
                        
        temp.append(int(str(N) * i))
        if number in temp:
            return i
        
        answer.append(list(set(temp)))
        
    return -1
                

print(solution(5, 12))
print(solution(2, 11))