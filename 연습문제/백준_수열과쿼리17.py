import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[end]
        return tree[node]
    mid = (start + end) // 2
    
    tree[node] = min(init(2*node, start, mid), init(2*node+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or start > right:
        return 2e9
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end) // 2
    return min(query(2*node, start, mid, left, right), query(2*node+1, mid+1, end, left,right))

def update(node, start, end, idx, value):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = value
        return
    
    mid = (start+end) // 2
    
    update(2*node, start, mid, idx, value)
    update(2*node+1, mid+1, end, idx, value)
    
    tree[node] = min(tree[2*node], tree[2*node+1])
    
if __name__ == "__main__":
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    num_ex = int(input())
    tree = [0 for _ in range(4*(n+1))]
    
    init(1,1,n)
    
    for _ in range(num_ex):
        commend, i, v = map(int, input().split())
        
        if commend == 1:
            update(1,1,n,i,v)
            arr[i] = v
        
        else:
            print(query(1,1,n,i,v))