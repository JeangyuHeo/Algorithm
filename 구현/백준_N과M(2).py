def dfs(start, cur_list):
    
    for i in range(start, n+1):
        if len(cur_list) == m - 1:
            print(*(cur_list+[i]))
        else:
            dfs(i+1, cur_list+[i])

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    dfs(1, [])