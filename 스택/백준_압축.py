import sys
input = sys.stdin.readline

if __name__ == "__main__":
    input_str = input()
    length = 0
    st = []
    dig = ''
    
    for ch in input_str.strip():
        if ch.isdigit():
            length+=1
            dig = ch
        elif ch == '(':
            st.append([dig, length-1])
            length = 0
        else:
            num, prev_length = st.pop()
            length = (int(num) * length) + prev_length
    
    print(length)