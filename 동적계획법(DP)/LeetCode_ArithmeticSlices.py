class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0 
        i = 0
        
        while i+2 < length:
            start = i
            while i+2 < length and nums[i+2] + nums[i] == 2*nums[i+1]:
                answer += i - start + 1
                i += 1
            i += 1

        return answer