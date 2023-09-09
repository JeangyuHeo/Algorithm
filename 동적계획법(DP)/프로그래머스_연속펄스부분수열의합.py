def solution(sequence):
    answer, code = 0, 1
    len_seq = len(sequence)
    dp = [[-1e9 for _ in range(len_seq)] for _ in range(2)]
    dp[0][0], dp[1][0] = sequence[0], -sequence[0]
    
    for i in range(1, len_seq):
        dp[0][i] = max(-code * sequence[i], dp[0][i-1] - code * sequence[i])
        dp[1][i] = max(code * sequence[i], dp[1][i-1] + code * sequence[i])
        code *= -1
    
    return max(max(dp[0]), max(dp[1]))

if __name__ == "__main__":
    print(solution([2, 3, -6, 1, 3, -1, 2, 4]), 10)