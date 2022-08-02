import math

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nums = []
        for _ in range(n//10 + 1):
            nums += list(map(int, input().split()))
        
        length = math.ceil(n/2)
        print(length)
        for i in range(length):
            if i!=0 and i%10 == 0:
                print()
            print(sorted(nums[:2*i+1])[i], end=' ')
        print()