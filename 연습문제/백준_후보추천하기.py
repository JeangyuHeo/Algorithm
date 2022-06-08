if __name__ == "__main__":
    n = int(input())
    re_num = int(input())
    re_info = list(map(int, input().split()))
    
    q = {}

    for i in range(re_num):
        if re_info[i] in q:
            q[re_info[i]][0] += 1
        else:
            if len(q) >= n:
                sorted_list = sorted(q.items(), key = lambda x: (x[1][0], x[1][1]))
                del(q[sorted_list[0][0]])
            q[re_info[i]] = [1,i]
        
    for i in sorted(q.keys()):
        print(i, end=' ')