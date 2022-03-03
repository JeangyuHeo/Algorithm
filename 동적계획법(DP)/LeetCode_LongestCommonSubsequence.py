def solution(text1:str, text2:str) -> int:
    text1_len, text2_len = len(text1), len(text2)    
    dp = [[0]* (text2_len+1) for _ in range(text1_len+1)]
    answer = 0
    
    for i in range(1, text1_len+1):
        for j in range(1, text2_len+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
    return dp[text1_len][text2_len]

print(solution("abcde", "ace"))
print(solution("abc", "abc"))
print(solution("abc", "def"))