if __name__ == "__main__":
    n = int(input())
    coordinates = [list(map(int, input().split())) for _ in range(n)]
    dp = [1e9 for _ in range(n+1)]
    dp[0] = 0
    
    for i in range(n):
        if coordinates[i][1] < 0:
            coordinates[i][1] *= -1
            
    coordinates.sort(key = lambda x: x[0])
    
    for i in range(0, n):
        y = 0
        for j in range(i, -1, -1):
            y= max(y, coordinates[j][1])
            length = max(coordinates[i][0]-coordinates[j][0], y * 2)
            dp[i+1] = min(dp[i+1], dp[j] + length)
            
    print(dp[n])