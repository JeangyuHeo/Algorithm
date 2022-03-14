def fibonacci(n):
    if d[n] != 0:
        return d[n]
    else:
        d[n] = fibonacci(n-2)+ fibonacci(n-1)
        return d[n]
    
num = int(input())
d = [1 if i ==1 or i==2 else 0 for i in range(num+1) ]

print(fibonacci(num))