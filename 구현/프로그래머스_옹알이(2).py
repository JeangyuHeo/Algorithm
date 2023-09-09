def solution(babbling):
    answer = 0
    able = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        for word in able:
            if word * 2 not in babble:
                babble = babble.replace(word, ' ')
        
        if babble.strip() == '':
            answer += 1
    
    return answer

if __name__ == "__main__":
    print(solution(["aya", "yee", "u", "maa"]), 1)
    print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]), 2)