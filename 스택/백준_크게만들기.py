import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(input().strip())
    st = []
    
    for num in nums:
        while st and st[-1] < num and k:
                st.pop()
                k-=1

        st.append(num)
        
    st = st[: len(st) - k]
    
    print("".join(st))