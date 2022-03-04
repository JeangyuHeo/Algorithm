def find_parents(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parents(parent[x])
        return parent[x]
    
def union(x,y):
    x = find_parents(x)
    y = find_parents(y)
    
    if parent[y] != parent[x]:
        parent[y] = x
        number[x] += number[y]
        
num_case = int(input())

for _ in range(num_case):
    num_relation = int(input())
    parent=dict()
    number=dict()
    
    for _ in range(num_relation):
        name1, name2 = input().split(" ")
        if name1 not in parent:
            parent[name1] = name1
            number[name1] = 1
            
        if name2 not in parent:
            parent[name2] = name2
            number[name2] = 1
            
        union(name1, name2)
        print(number[find_parents(name1)])