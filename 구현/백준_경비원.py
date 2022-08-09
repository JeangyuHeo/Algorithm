

if __name__ == "__main__":
    answer = 0
    m, n = map(int, input().split())
    total = int(input())
    #1 북, 2 남, 3 서, 4 동
    pos = [list(map(int, input().split())) for _ in range(total)]
    dong = list(map(int, input().split()))
    
    for dir, idx in pos:
        min_dist = 1e9
        if dir == 1:
            if dong[0]==1:
                min_dist = min(min_dist, abs(idx-dong[1]))
            elif dong[0] == 2:
                min_dist = min(min_dist, n+idx+dong[1], n+m-idx+m-dong[1])
            elif dong[0] == 3:
                min_dist = min(min_dist, dong[1]+idx)
            elif dong[0] == 4:
                min_dist = min(min_dist, m-idx+dong[1])
                
        elif dir == 2:
            if dong[0]==1:
                min_dist = min(min_dist, n+idx+dong[1], n+m-idx+m-dong[1])
            elif dong[0]==2:
                min_dist= min(min_dist, abs(idx-dong[1]))
            elif dong[0]==3:
                min_dist = min(min_dist, n-dong[1]+idx)
            elif dong[0]==4:
                min_dist = min(min_dist, m-idx+ n-dong[1])
            
        elif dir == 3:
            if dong[0]==1:
                min_dist = min(min_dist, idx+dong[1])
            elif dong[0]==2:
                min_dist = min(min_dist, n-idx+dong[1])
            elif dong[0]==3:
                min_dist = min(min_dist, abs(dong[1] - idx))
            elif dong[0]==4:
                min_dist = min(min_dist, idx+dong[1]+m, n-idx+n-dong[1]+m)

        else:
            if dong[0]==1:
                min_dist= min(min_dist, m-dong[1]+idx)
            elif dong[0]==2:
                min_dist = min(min_dist, m-dong[1]+n-idx)
            elif dong[0]==3:
                min_dist = min(min_dist, m+idx+dong[1], m+n-idx+n-dong[1])
            elif dong[0]==4:
                min_dist = min(min_dist, abs(idx-dong[1]))
            
        answer += min_dist
        
    print(answer)
    