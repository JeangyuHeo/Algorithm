def solution(babbling):
    answer = 0
    able = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        for word in able:
            babble = babble.replace(word, " ")
        if babble.strip() == "":
            answer += 1
    
    return answer

if __name__ == "__main__":
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]), 1)
    print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]), 3)