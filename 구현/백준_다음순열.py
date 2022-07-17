import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    swap_idx = -1
    
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            swap_idx = i - 1
            break
            
    if swap_idx == -1:
        print(-1)
        sys.exit()
        
    for i in range(n-1, 0, -1):
        if nums[swap_idx] < nums[i]:
            nums[swap_idx], nums[i] = nums[i], nums[swap_idx]
            nums = nums[:swap_idx+1] + sorted(nums[swap_idx+1:])
            print(*nums)
            break