def solution(weight):
    total, answer = 0, 1
    weight.sort()

    for w in weight:
        if total + w > 3:
            answer +=1
            total = w
        else:
            total += w
        
    return answer

print(solution([1.4, 1.01, 2.4, 1.01, 1.01]))