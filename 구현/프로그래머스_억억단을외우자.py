def solution(e, starts):
    answer = []
    counts = [0 for i in range(e+1)]
    
    for i in range(1, e+1):
        for j in range(i+1, e+1):
            multi = i*j
            if multi > e:
                break
            if i == j:
                counts[multi] += 1
            else:
                counts[multi] += 2
    
    max_val = 0
    dp = [0 for _ in range(e+1)]
    
    for i in range(e, 0, -1):
        if max_val <= counts[i]:
            max_val = counts[i]
            dp[i] = i
        else:
            dp[i] = dp[i+1]

    return [dp[start] for start in starts]

if __name__ == "__main__":
    print(solution(8, [1,3,7]))