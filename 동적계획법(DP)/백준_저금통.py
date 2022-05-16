def get_prime(n):
    
    for i in range(2, make_number(n,n)+1):
        if is_prime[i]:
            for j in range(2*i, make_number(n,n)+1, i):
                is_prime[j] = 0

def make_number(first, second):
    length = len(str(second))
    return first * (10**length) + second

if __name__ == "__main__":
    answer = 0
    n = int(input())
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    is_prime = [0, 0] + ([1] * (make_number(n,n)-1))

    get_prime(n)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==1 and j==1:
                continue
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + is_prime[make_number(i,j)]

    print(dp[n][n])
    #print(max(dp[n][n-1], dp[n-1][n]))