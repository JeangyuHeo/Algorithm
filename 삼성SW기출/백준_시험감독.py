from math import ceil


if __name__ == "__main__":
    answer = 0
    n = int(input())
    nop = list(map(int, input().split(' ')))
    first, second = map(int, input().split(' '))
    
    for i in range(n):
        if nop[i] > 0:
            nop[i] -= first
            answer+=1
        if nop[i] > 0:
            answer += ceil(nop[i] / second)
        
    print(answer)