def compare_char(left, right):
    if left >= right:
        return True
    
    if s[left] < s[right]:
        return True
    elif s[left] > s[right]:
        return False
    else:
        return compare_char(left+1, right-1)
    

if __name__ == "__main__":
    answer=''
    n = int(input())
    s = [input() for _ in range(n)]

    left, right = 0, n-1
    
    for i in range(n):
        if i % 80 == 0 and i != 0:
            answer+='\n'
        if compare_char(left, right):
            answer+=s[left]
            left+=1
        else:
            answer+=s[right]
            right-=1

    print(answer)