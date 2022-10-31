import sys

input = sys.stdin.readline

def dfs(i, j):
    if i == 0 or j == 0:
        return
    if str1[i] == str2[j]:
        dfs(i-1, j-1)
        print(str1[i], end='')

    else:
        if dp[i][j-1] == dp[i][j]:
            dfs(i, j-1)
        else:
            dfs(i-1, j)


if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()

    len_str1 = len(str1)
    len_str2 = len(str2)

    str1 = '0'+str1
    str2 = '0'+str2

    dp = [[0 for _ in range(42)] for _ in range(42)]

    for i in range(1, len_str1+1):
        for j in range(1, len_str2+1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    dfs(len_str1, len_str2)

