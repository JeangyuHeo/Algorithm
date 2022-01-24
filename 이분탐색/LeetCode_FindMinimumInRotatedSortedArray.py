class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        
        while start <= end:
            avg = (start + end) // 2
            
            if nums[avg] == nums[end]:
                end -= 1
            elif nums[avg] > nums[end]:
                start = avg + 1
            else:
                end = avg
                
        return nums[end+1]