def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight=0
    q=[]
    
    for truck_weight in truck_weights:
        
        while True:
            if not q:
                q.append(truck_weight)
                total_weight+=truck_weight
                answer+=1
                break
            elif len(q) == bridge_length:
                total_weight-=q.pop(0)
            else:
                if total_weight + truck_weight > weight:
                    q.append(0)
                    answer+=1
                else:
                    q.append(truck_weight)
                    total_weight+=truck_weight
                    answer+=1
                    break
                    
    answer+=bridge_length
    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))