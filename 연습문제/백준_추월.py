

if __name__ == "__main__":
    answer = 0
    n = int(input())
    dict = {}
    
    for i in range(n):
        daegeun = input()
        dict[daegeun] = i
    
    car_to_idx = []
    
    for i in range(n):
        youngsik = input()
        car_to_idx.append(dict[youngsik])
        
    for i in range(n-1):
        for j in range(i+1, n):
            if car_to_idx[i] > car_to_idx[j]:
                answer+=1
                break
            
    print(answer)