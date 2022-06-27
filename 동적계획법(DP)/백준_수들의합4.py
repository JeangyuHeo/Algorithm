from collections import defaultdict

if __name__ == "__main__":
    answer=0
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    dict = defaultdict(int)
    
    for i in range(1, n):
        nums[i] += nums[i-1]
    
    for i in range(n):
        if nums[i] == k:
            answer += 1
        answer += dict[nums[i]-k]
        dict[nums[i]] += 1
        
    print(answer)