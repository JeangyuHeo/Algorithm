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
                answer = max(answer, dp[k_pos+K-1] + dp[l_pos+L-1] - dp[l_pos-1])
            else:
                answer = max(answer, dp[k_pos+K-1] - dp[k_pos-1] + dp[l_pos+L-1] - dp[l_pos-1])
    
    for l_pos in range(n-(L+K-1)):
        for k_pos in range(l_pos+L, n-K+1):
            if l_pos == 0:
                answer = max(answer, dp[l_pos+L-1] + dp[k_pos+K-1] - dp[k_pos-1])
            else:
                answer = max(answer, dp[l_pos+L-1] - dp[l_pos-1] + dp[k_pos+K-1] - dp[k_pos-1])

    return answer

if __name__ == "__main__":
    test_case_1 = [6, 1, 4, 6, 3, 2, 7, 4]
    answer_1 = 24

    test_case_2 = [10, 19, 15]
    answer_2 = -1
    
    print("결과 값:",solution(test_case_1, 3, 2),"정답:", answer_1)
    print("결과 값:",solution(test_case_2, 2, 2),"정답:", answer_2)