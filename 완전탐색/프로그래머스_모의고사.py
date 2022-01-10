def solution(answers):
    loser=[]
    loser.append([1, 2, 3, 4, 5])
    loser.append([2,1,2,3,2,4,2,5])
    loser.append([3,3,1,1,2,2,4,4,5,5])
    score=[0,0,0]
    answer = []
    
    for idx, ans in enumerate(answers):
        for i in range(3):
            if ans == loser[i][idx % len(loser[i])]:
                score[i]+=1
    
    idx = score.index(max(score))
    
    for i in range(3):
        if score[i] == score[idx]:
            answer.append(i+1)
    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))