def solution(word1:str, word2:str) -> int:
    answer, screen_size = 0, 0
    
    if len(word1) <= len(word2):
        screen_size = len(word1)
    else:
        screen_size = len(word2)
        word1, word2 = word2, word1
    
    while screen_size > 0:
        for i in range(len(word1) - screen_size+1):
            tmp = word1[i:screen_size+1]
            if tmp in word2:
                print(tmp)
                return len(word1) + len(word2) - (2* screen_size)
        
        screen_size-=1
    
    return answer

print(solution("sea", "eat"))
print(solution("leetcode", "etco"))