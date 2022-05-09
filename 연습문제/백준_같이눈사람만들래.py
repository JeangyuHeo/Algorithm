import sys

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))
    
    d.sort()
    
    answer = 1e9
    
    for i in range(n-3):
        for j in range(i+3,n):
            snow_man_1 = d[i] + d[j]
            left = i + 1
            right = j - 1
            
        while left < right:
            cand = d[left] + d[right]
            diff = abs(snow_man_1 - cand)
            if diff < answer:
                answer = diff
            
            if snow_man_1 > cand:
                left += 1
            elif snow_man_1 < cand:
                right -= 1
            else:
                print(0)
                sys.exit(0)
    print(answer)