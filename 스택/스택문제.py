def solution(arr :list):
    if len(set(arr)) == 1:
        return 1
    
    st = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            st.append(arr[i])

    answer = 2
    
    for i in range(1, len(st)-1):
        if st[i] > st[i-1] and st[i] > st[i+1]:
            answer += 1
        
        if st[i] < st[i-1] and st[i] < st[i+1]:
            answer += 1
        
    return answer
    

if __name__ == "__main__":
    print(solution([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]))
    print(solution([-3, -3]))