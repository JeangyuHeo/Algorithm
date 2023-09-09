def solution(scores):
    
    if len(list(filter(lambda x: x[0] > scores[0][0] and x[1] > scores[0][1], scores[1:]))) != 0:
        return -1
    
    answer = 1
    wanho_score = scores[0][0] + scores[0][1]
    
    scores.sort(key = lambda x: (-x[0], x[1]))
    
    max_num = 0
    
    for score1, score2 in scores:
        if max_num <= score2:
            if wanho_score < score1 + score2:
                answer += 1
            max_num = score2
    
    return answer
    
    

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
print(solution([[2,3],[2,2],[2,2],[2,2],[2,2]]))
print(solution([[2,2],[1,3],[3,1],[1,3],[3,1]]))
print(solution([[3,1],[2,3],[2,2], [2,3], [1,0], [1,0], [1,4], [1,5]]))
print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]))
print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))