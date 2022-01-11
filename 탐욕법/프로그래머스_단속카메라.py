def solution(routes):
    answer = 1
    
    routes.sort()
    
    nearest = routes[0][1]
    
    for i in range(0, len(routes)-1):
        if nearest < routes[i+1][0]:
            answer+=1
            nearest = routes[i+1][1]
        nearest = min(routes[i+1][1], nearest)
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))