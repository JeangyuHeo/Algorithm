class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_point = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last_point:
                last_point = i
                
        return last_point == 0