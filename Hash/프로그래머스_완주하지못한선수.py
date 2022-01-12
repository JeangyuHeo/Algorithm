from collections import defaultdict

def solution(participant, completion):
    answer = ''
    completions = defaultdict(int)
    
    for c in completion:
        completions[c]+=1
    
    for p in participant:
        if ((p not in completions.keys()) or (completions[p] ==0)):
            return p
        else:
            completions[p]-=1
    
    return answer