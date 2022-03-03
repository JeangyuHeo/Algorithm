n,m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

answer = -1

for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = data[i] + data[j] + data[k]
            if (sum <= m) and (sum > answer):
                answer = sum
                
print(answer)