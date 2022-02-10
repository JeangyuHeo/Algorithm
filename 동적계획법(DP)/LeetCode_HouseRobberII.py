class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        def max_money(nums):
            nums = [0] + nums
            for i in range(3,len(nums)):
                nums[i] += max(nums[i-3],nums[i-2])
                
            return max(nums[-1],nums[-2])
    
        return max(max_money(nums[1:]),max_money(nums[:-1])) if len(nums) > 2 else max(nums)