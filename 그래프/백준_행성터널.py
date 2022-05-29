def find_parents(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find_parents(parents[x])
        return parents[x]
    
def union_node(x,y):
    p_x = find_parents(x)
    p_y = find_parents(y)
    
    if p_x > p_y:
        parents[p_x] = p_y
    else:
        parents[p_y] = p_x

def calc_cost(cordi):
    tunnel = []
    
    for i in range(n-1):
        cost = abs(cordi[i][0] - cordi[i+1][0])
        tunnel.append([cordi[i][1], cordi[i+1][1], cost])
    
    return tunnel

if __name__ == "__main__":
    answer=0
    n = int(input())
    parents = [i for i in range(n)]
    
    x_cord, y_cord, z_cord = [], [], []
    
    for i in range(n):
        x,y,z = map(int, input().split())
        x_cord.append([x,i])
        y_cord.append([y,i])
        z_cord.append([z,i])
    
    x_cord.sort(key=lambda x: x[0])
    y_cord.sort(key=lambda x: x[0])
    z_cord.sort(key=lambda x: x[0])
    
    tunnel = []

    tunnel.extend(calc_cost(x_cord))
    tunnel.extend(calc_cost(y_cord))
    tunnel.extend(calc_cost(z_cord))
    
    tunnel.sort(key = lambda x : x[2])
    
    for x, y, cost in tunnel:
        if find_parents(x) != find_parents(y):
            union_node(x,y)
            answer+=cost
            
    print(answer)