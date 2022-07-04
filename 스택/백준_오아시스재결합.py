import sys

input = sys.stdin.readline

if __name__ == "__main__":
    answer = 0
    n = int(input())
    people = [int(input()) for _ in range(n)]
    
    st = []
    
    for height in people:
        while st and st[-1][0] < height:
            answer += st.pop()[1]
            
        if not st:
            st.append([height, 1])
            continue
        if st[-1][0] == height:
            cnt = st.pop()[1]
            answer += cnt
            
            if st:
                answer += 1
                
            st.append([height, cnt+1])
        
        else:
            st.append([height, 1])
            answer+=1
            
    print(answer)