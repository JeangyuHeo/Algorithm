def solution(s, skip, index):
    candidates = "abcdefghijklmnopqrstuvwxyz"
    
    for sk in skip:
        candidates = candidates.replace(sk, "")

    return "".join([candidates[(candidates.index(ch)+index)%len(candidates)] for ch in s])

print(solution("aukks", "wbqd", 5))