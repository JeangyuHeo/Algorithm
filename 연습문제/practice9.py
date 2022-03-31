def solution(money, costs):
    answer = 0
    cost_list = []
    
    coin_size = 0
    for idx, cost in enumerate(costs):
        if coin_size == 0:
            coin_size += 1
        elif idx % 2:
            coin_size *= 5
        else:
            coin_size *= 2
        
        cost_list.append((coin_size, cost))
    
    cost_list.sort(key = lambda x: x[1] / x[0])
    
    for size, cost in cost_list:
        answer += cost * (money // size)
        money -= size * (money // size)
        
    return answer


print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))