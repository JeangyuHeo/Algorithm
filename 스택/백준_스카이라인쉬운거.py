if __name__ == "__main__":
    answer = 0
    n = int(input())
    heights = [list(map(int, input().split())) for _ in range(n)]
    
    st = [0]
    
    for x, height in heights:
        if height > st[-1]:
            answer +=1
            st.append(height)
            
        else:
            while st[-1] > height:
                st.pop()
                
            if st[-1] < height:
                answer += 1
                st.append(height)
                
    print(answer)