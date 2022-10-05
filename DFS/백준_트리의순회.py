import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def pre_order(in_s, in_e, post_s, post_e):
    
    if in_s > in_e or post_s > post_e:
        return
    
    root = post_order[post_e]
    
    print(root, end=' ')
    
    pre_order(in_s, in_idx[root]-1, post_s, post_s + in_idx[root]-in_s-1)
    pre_order(in_idx[root]+1, in_e, post_s+in_idx[root]-in_s, post_e - 1)
        

if __name__ == "__main__":
    n = int(input())
    
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    
    root = post_order[-1]
    
    in_idx = [0 for _ in range(n+1)]
    
    for i in range(n):
        in_idx[in_order[i]] = i
    
    pre_order(0, n-1, 0, n-1)