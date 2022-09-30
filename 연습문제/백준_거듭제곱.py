if __name__ == "__main__":
    answer = 0
    n = int(input())
    s=''
    while n > 0:
        s+=str(n%2)
        n//=2
    
    for i in range(len(s)):
        if s[i] == '1':
            answer += 3 ** i
    print(answer)