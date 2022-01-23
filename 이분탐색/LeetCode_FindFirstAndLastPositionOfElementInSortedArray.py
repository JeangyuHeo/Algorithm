class Solution:
    def binary_Search(self, nums, target, isStart):
        start = 0
        end = len(nums) - 1
        result = -1
        
        while start <= end:
            avg = (start + end) // 2
            
            if nums[avg] > target:
                end = avg - 1
            elif nums[avg] < target:
                start = avg + 1
            else:
                if isStart:
                    result = avg
                    end = avg - 1
                else:
                    result = avg
                    start = avg + 1
                
        return result
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binary_Search(nums, target, True), self.binary_Search(nums, target, False)]