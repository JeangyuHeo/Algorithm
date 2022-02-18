class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        answer=0
        length = len(nums)
        dp = [1 for _ in range(length)]
        cnt = [1 for _ in range(length)]

        for i in range(1, length):
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                        
        return sum([c for idx, c in enumerate(cnt) if dp[idx] == max(dp)])