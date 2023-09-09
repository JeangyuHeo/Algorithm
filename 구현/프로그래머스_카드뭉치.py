def solution(cards1, cards2, goal):
    
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.pop(0)
        elif cards2 and word == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    
    return "Yes"

def solution2(cards1, cards2, goal):
    idx1, idx2 = 0, 0
    len_1, len_2 = len(cards1), len(cards2)
    
    for word in goal:
        if idx1 < len_1 and word == cards1[idx1]:
            idx1+=1
        elif idx2 < len_2 and word == cards2[idx2]:
            idx2+=1
        else:
            return "No"
    
    return "Yes"

if __name__ == "__main__":
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))