def solution(sentence, keyword, skips):
    answer=""
    
    sent_len, key_len, cur = len(sentence), len(keyword), 0

    for idx, skip in enumerate(skips):
        tmp_sent = sentence[cur:cur+skip]
        tmp_key = keyword[idx % key_len]
        update_idx, update_str = 0, ""

        if tmp_key in tmp_sent:
            find = tmp_sent.find(tmp_key)
            update_str = tmp_sent[:find+1]+tmp_key
            update_idx = find+1
        else:
            if cur + skip <= sent_len:
                update_str = tmp_sent + tmp_key
                update_idx = skip
        
        answer += update_str
        cur += update_idx
        
    return answer + sentence[cur:]

#Test cases
sentence = "i love coding"
keyword = "mask"
skips = [0, 0, 3, 2, 3, 4]
# "mai lsovke cmodinag"
print(solution(sentence, keyword, skips))

sentence = "i love coding"
keyword = "mode"
skips = [0, 10]
# "mi loove coding"
print(solution(sentence, keyword, skips))

sentence = "abcde fghi"
keyword = "axyz"
skips = [3, 9, 0, 1]
# "aabcde fghixy"
print(solution(sentence, keyword, skips))

sentence = "encrypt this sentence"
keyword = "something"
skips = [0, 1, 3, 2,9,2,0,3,0,2,4,1,3]
# "seoncrmypett thihisng ssenteonmcee"
print(solution(sentence, keyword, skips))