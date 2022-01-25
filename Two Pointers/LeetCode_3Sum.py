class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        length = len(nums)
        nums.sort()
        
        for i in range(length-2):
            left = i+1
            right = length-1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    candidate = [nums[i], nums[left], nums[right]]
                    if candidate not in answer:
                        answer.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
        return answer