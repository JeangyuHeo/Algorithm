def solution(answers):
    loser=[
        [1, 2, 3, 4, 5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    score=[0,0,0]

    
    for idx, ans in enumerate(answers):
        for i in range(3):
            if ans == loser[i][idx % len(loser[i])]:
                score[i]+=1
    
    idx = score.index(max(score))
    
    return [i+1 for i in range(3) if score[i] == score[idx]]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))