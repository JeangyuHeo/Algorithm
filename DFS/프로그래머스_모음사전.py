alphabet = ['A', 'E', 'I', 'O', 'U']
cnt = 0

def dfs(w, depth):
    global cnt
    if depth == 6:
        return
    
    cnt+=1
    
    for a in alphabet:
        dic[w+a] = cnt
        dfs(w+a, depth+1)
    
def solution(word):
    global answer, dic
    answer = 0
    dic = {}
    
    dfs("", 0)
    
    return dic[word]

print(solution("AAAAE"))
cnt=0
print(solution("AAAE"))
cnt=0
print(solution("I"))
cnt=0
print(solution("EIO"))