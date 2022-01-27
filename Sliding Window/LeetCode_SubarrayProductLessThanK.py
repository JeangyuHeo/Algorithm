class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        total = 1
        answer = left = 0
        
        for i in range(len(nums)):
            total *= nums[i]
            while total >= k:
                total /= nums[left]
                left +=1
            answer += i + 1 - left
        
        return answer