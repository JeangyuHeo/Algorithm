class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [i==0 for i in range(length+1)]
        
        for i in range(1, length+1):
            for j in range(i):
                print(i,j,dp[j], s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        return dp[-1]