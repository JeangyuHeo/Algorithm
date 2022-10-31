import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    answer = []
    st = []
    
    cnt = 1
    
    for _ in range(n):
        num = int(input())
        while cnt <= num:
            st.append(cnt)
            cnt += 1
            answer.append('+')
        if st[-1] == num:
            answer.append('-')
            st.pop()
        else:
            print('NO')
            exit()
    
    print("\n".join(answer))