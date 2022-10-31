import sys

input = sys.stdin.readline

if __name__ == "__main__":
    test_case = int(input())
    
    for _ in range(test_case):
        st = []
        tmp = []
        info = list(input().strip())
        
        for log in info:
            if log == '<':
                if st:
                    tmp.append(st.pop())
            elif log == '>':
                if tmp:
                    st.append(tmp.pop())
            elif log == '-':
                if st:
                    st.pop()
            else:
                st.append(log)
                
        print("".join(st+tmp[::-1]))