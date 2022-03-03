n = int(input())
result, stack = [], []

count = 1

for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        count+=1
        result.append('+')
    if stack[-1] == num:
        result.append('-')
        stack.pop()
    else:
        print('NO')
        exit(0)
        
print('\n'.join(result))