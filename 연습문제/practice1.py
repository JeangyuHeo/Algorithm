import heapq

def solution(cards):
    answer = 0
    length = len(cards)
    visited = []

    for i in range(length):
        if i not in visited:
            min_idx = cards[i].index(min(cards[i]))
            for j in range(i+1, length):
                if j not in visited:
                    tmp_min_idx = cards[j].index(min(cards[j]))
                    if min_idx == tmp_min_idx:
                        continue
                    cards[i][min_idx]+=1
                    cards[i][tmp_min_idx]-=1
                    cards[j][min_idx]-=1
                    cards[j][tmp_min_idx]+=1
                    visited += [i, j]
                    break
                    # if min(card1) > cards[i][min_idx] and min(card2) > cards[j][tmp_min_idx]:
                    #     cards[i][min_idx]+=1
                    #     cards[i][tmp_min_idx]-=1
                    #     cards[j][min_idx]-=1
                    #     cards[j][tmp_min_idx]+=1
                    #     visited += [i, j]
                    #     break
        answer += min(cards[i])
    return answer if answer >=0 else 0

#test case
cards1 = [[10, 5, 15], [5, 15, 10], [10, 11, 9]] # 21
cards2 = [[10, 5, 15], [8, 9, 13], [10, 10, 10]] # 23
cards3 = [[ 8,11, 11], [6, 15, 9], [14, 2, 14], [8, 20, 2]] # 22
cards4 = [[ 8,11, 11], [10, 7, 13], [15, 10, 5], [7, 17, 6]] # 28
cards5 = [[0, 0, 30], [30, 0, 0]] # 0

print(solution(cards1))
print(solution(cards2))
print(solution(cards3))
print(solution(cards4))
print(solution(cards5))