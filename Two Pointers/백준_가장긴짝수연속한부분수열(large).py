import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    s = list(map(int, input().strip().split()))
    
    left, right = 0, -1
    answer, odd_cnt = 0, 0
    tmp_cnt = 0
    
    while True:
        if odd_cnt <= k:
            answer = max(answer, tmp_cnt - odd_cnt)
            
        if odd_cnt <= k:
            right += 1
            if right >= n:
                break
            
            if s[right] % 2 == 1:
                odd_cnt += 1
            tmp_cnt += 1
        
        else:
            if s[left] % 2 == 1:
                odd_cnt -= 1
            tmp_cnt -= 1
            
            left += 1
            if left > right:
                break
            
    print(answer)