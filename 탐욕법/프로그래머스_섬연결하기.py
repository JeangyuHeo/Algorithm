parents = [0] * 100

def find_parent(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find_parent(parents[x])
        return parents[x]

def union_node(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a<b:
        parents[b] = a
    else:
        parents[a] = b
        
def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x: x[2])
    
    for i in range(n):
        parents[i] = i
        
    for cost in costs:
        if find_parent(cost[0]) != find_parent(cost[1]):
            union_node(cost[0], cost[1])
            answer+=cost[2]
    
    return answer