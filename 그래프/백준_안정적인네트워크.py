def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union_node(x,y):
    x_p = find_parent(x)
    y_p = find_parent(y)
    
    if x_p < y_p:
        parents[y_p] = x_p
    elif x_p > y_p:
        parents[x_p] = y_p
    else:
        return -1,-1

    return x,y

if __name__ == "__main__":
    total_cost = 0
    result_cnt = 0
    n,m = map(int,input().split())
    parents = [i for i in range(n+1)]

    for _ in range(m):
        x,y = map(int, input().split())
        union_node(x,y)
    
    cost = [list(map(int, input().split())) for _ in range(n)]
    
    costs = []
    
    for i in range(n):
        for j in range(i+1, n):
            costs.append([i+1,j+1, cost[i][j]])
            
    costs.sort(key=lambda x: x[2])
    
    result = []
    
    for x,y,c in costs:
        if x == 1:
            continue
        if find_parent(x) != find_parent(y):
            _x, _y = union_node(x,y)
            total_cost+=c
            result_cnt+=1
            result.append([x,y])
    
    print(total_cost, result_cnt)
    for x,y in result:
        print(y,x)