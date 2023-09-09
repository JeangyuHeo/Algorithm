import sys

input = sys.stdin.readline

def find_before(i):
    global nums
    
    for j in range(n-1, 0, -1):
        if nums[j] < nums[i-1]:
            nums[j], nums[i-1] = nums[i-1], nums[j]
            nums = nums[:i] + sorted(nums[i:], reverse=True)
            print(*nums)
            return True
    return False
    
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().strip().split()))

    for i in range(n-1, 0, -1):
        if nums[i] < nums[i-1]:
            if find_before(i):
                break
    else:
        print(-1)