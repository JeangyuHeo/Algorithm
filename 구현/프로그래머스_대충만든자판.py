def solution(keymap, targets):
    key_dict = {alpha: 1e9 for alpha in list(map(chr, range(65, 91)))}
    answer = []

    for keyboard in keymap:
        for i in range(len(keyboard)):
            key_dict[keyboard[i]] = min(key_dict[keyboard[i]], i+1)
    
    for target in targets:
        cur_result = 0
        for alpha in target:
            cur_result += key_dict[alpha]
        answer.append(-1 if cur_result >= 1e9 else cur_result)
        
    return answer

if __name__ == "__main__":
    print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
    print(solution(["AA"], ["B"]))
    print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))