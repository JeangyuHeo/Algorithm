class Solution:
    def jump(self, nums: List[int]) -> int:
        q = [0]
        length = len(nums)
        dp = [0] * length

        for index in range(length):
            for jump_limit in range(1, nums[index]+1):
                if index +jump_limit < length:
                    if dp[index + jump_limit] == 0:
                        dp[index + jump_limit] = dp[index] + 1
        
        return dp[-1]