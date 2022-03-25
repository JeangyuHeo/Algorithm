def solution(money, costs):
    i,answer = 1,0
    cost_per = []

    for idx, cost in enumerate(costs):
        if idx%2:
            i *= 5
        elif idx%2==0 and idx!=0:
            i *= 2
        cost_per.append((i, cost))

    cost_per.sort(reverse=True, key=lambda x: x[0]/x[1])

    for unit, cost in cost_per:
        answer += (money // unit) * cost
        money = money % unit

    return answer