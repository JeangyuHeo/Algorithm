def check_diff(cur, other):
    cnt=0
    for i in range(len(cur)):
        if cur[i] != other[i]:
            cnt+=1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    visited = [False] * len(words)
    answer = 1e9
    
    def DFS(cur, count):
        if cur == target:
            nonlocal answer
            answer = min(answer, count)
            return
        
        for idx, word in enumerate(words):
            if all([check_diff(cur, word), not visited[idx]]):
                visited[idx] = True
                DFS(word, count+1)
                visited[idx] = False
                
    if target not in words:
        return 0
    
    DFS(begin, 0)
    
    return answer

print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log"]))