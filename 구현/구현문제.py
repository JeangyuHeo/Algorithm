def solution(A, K, L):
    n = len(A)
    if n < K+L: 
        return -1
    
    dp = [A[0]]
    
    for i in range(1, n):
        dp.append(dp[i-1] + A[i])
    
    answer = 0
    
    for k_pos in range(n-(L+K-1)):
        for l_pos in range(k_pos+K, n - L+1):
            if k_pos == 0:
                answer = max(answer, dp[k_pos+K-1] - dp[k_pos] + dp[l_pos+L-1] - dp[l_pos-1])
            else:
                answer = max(answer, dp[k_pos+K-1] - dp[k_pos-1] + dp[l_pos+L-1] - dp[l_pos-1])
    
    return answer

if __name__ == '__main__':
    print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2)) # 24
    print(solution([10, 19, 15], 2, 2)) # -1