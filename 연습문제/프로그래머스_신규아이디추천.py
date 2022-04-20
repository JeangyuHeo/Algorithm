def solution(new_id):
    answer = ''
    
    # 소문자, 숫자, -, _, .(처음과 끝에 사용 x, 연속 사용 x) 만 가능
    
    #1단계 소문자 치환
    new_id = new_id.lower()
    
    #2단계 특수문자 제거
    new_id = "".join([ch for ch in new_id if '0'<=ch<='9' or 'a'<=ch<='z' or ch =='-' or ch == '_' or ch == '.'])
    
    #3단계 연속된 .. 을 .으로 치환
    flag = True
    
    for ch in new_id:
        if flag and ch == '.':
            flag = False
            answer+='.'
        elif (not flag) and ch == '.':
            continue
        elif ch !='.':
            flag = True
            answer+=ch
            
    # 처음에 위치한 '.' 제거
    if answer[0] == '.':
        answer = answer[1:]

    # 끝에 위치한 '.' 제거
    if len(answer)>0 and answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) == 0:
        answer += 'a'
    if len(answer) > 15:
        answer = answer[:15]
        
        #끝에 '.' 제거
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) < 3:
        answer+=answer[-1]
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))