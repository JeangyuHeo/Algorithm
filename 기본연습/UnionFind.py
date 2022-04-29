def find_parent(num):
    if num == parents[num]:
        return num
    else:
        parents[num] = find_parent(parents[num])
        return parents[num]
        
def union_node(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    
if __name__ == "__main__":
    graph = [
        [0,1,1],
        [0,2,2],
        [1,2,5],
        [1,3,1],
        [2,3,8] 
    ]
    answer = 0
    parents = [i for i in range(10)]
    
    graph.sort(key= lambda x: x[2])

    for node1, node2, cost in graph:
        if find_parent(node1) != find_parent(node2):
            union_node(node1, node2)
            answer += cost
            
    print(answer)