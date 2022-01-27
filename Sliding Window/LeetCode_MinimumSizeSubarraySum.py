class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        answer = 1e9
        total = left = 0
        
        for i in range(length):
            total += nums[i]
            while total >= target:
                answer = min(answer, i+1 - left)
                total -= nums[left]
                left += 1

        return 0 if answer == 1e9 else answer