import sys

input = sys.stdin.readline

if __name__ == "__main__":
    answer = 0
    n = int(input())
    work = list(input().strip())
    
    cnt_b, cnt_r = 0, 0
     
    for i in range(n):
        if i == 0:
            if work[i] == 'B': cnt_b+=1
            else: cnt_r+=1
            
        elif work[i] != work[i-1]:
            if work[i] == 'R':
                cnt_r += 1
            else:
                cnt_b += 1
    
    
    print(min(cnt_r, cnt_b)+1)