class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [1,1]
        
        if s[0] == '0':
            return 0
        
        for i in range(2, length+1):
            count=0
            if s[i-1] >= '1':
                count += dp[i-1]
            if s[i-2] != '0' and int(s[i-2: i]) <= 26:
                count += dp[i-2]
            dp.append(count)

        return dp[-1]