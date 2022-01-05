def solution(s):
    answer = 1e9
    
    for idx in range(1, len(s)//2+1):
        res=''
        cnt=1
        tmp = s[:idx]
        
        for i in range(idx, len(s)+idx, idx):
            if tmp == s[i: i+idx]:
                cnt+=1
            else:
                if cnt==1:
                    res+=tmp
                else:
                    res+=str(cnt)+tmp
                tmp = s[i: i+idx]
                cnt=1
        answer=min(answer, len(res))
        
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))