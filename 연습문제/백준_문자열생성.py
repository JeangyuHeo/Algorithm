from collections import deque

def check_alpha(l, r):
    
    if l >= r:
        return True

    if s[l] < s[r]:
        return True
    elif s[l] > s[r]:
        return False
    else:
        return check_alpha(l+1, r-1)
    
if __name__ == "__main__":
    n = int(input())
    s = deque([input() for _ in range(n)])
    
    result = ''
    
    left, right = 0, n-1

    for i in range(n):
        if i % 80 == 0 and i != 0:
            result+='\n'
        if check_alpha(left,right):
            result+=s[left]
            left+=1
        else:
            result+=s[right]
            right-=1

    print(result)