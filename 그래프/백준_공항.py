from gettext import find


def find_parent(x):
    if parents[x] == x:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]
    
def union_node(x,y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y    

if __name__ == "__main__":
    answer = 0
    
    g = int(input())
    p = int(input())
    parents = [i for i in range(g+1)]
    planes = [int(input()) for _ in range(p)]
    
    for plane in planes:
        x = find_parent(plane)
        
        if x==0:
            break
        union_node(x, x-1)
        answer += 1
        
    print(answer)