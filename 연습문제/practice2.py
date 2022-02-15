def solution(sentence, keyword, skips):
    answer=""
    sent_len, skips_len = len(sentence), len(skips)
    idx, skip_idx, sent_idx = 0, 0, 0
    
    for i in range(1, skips_len):
        skips[i] = skips[i-1]+skips[i]

    while True:
        print(skip_idx, sent_idx)
        if skip_idx >= skips_len and sent_idx >= sent_len:
            break
        while skip_idx < skips_len and skips[skip_idx] == idx:
            answer+=keyword[skip_idx%len(keyword)]
            skip_idx+=1
            
        if sent_idx < sent_len:
            answer+=sentence[sent_idx]
            if skip_idx < skips_len and sentence[sent_idx] == keyword[skip_idx%len(keyword)]:
                answer+=keyword[skip_idx%len(keyword)]
                skip_idx+=1
                
        sent_idx+=1
        idx+=1
        
    return answer

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