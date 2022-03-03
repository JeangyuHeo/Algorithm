case = int(input())

for _ in range(case):
    n,m = map(int, input().split(' '))
    weight = list(map(int, input().split(' ')))
    cnt = 0
    q = [(i, w) for i, w in enumerate(weight)]
    
    while q:
        if q[0][1] == max(q, key = lambda x: x[1])[1]:
            cnt += 1
            if q[0][0] == m:
                print(cnt)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))