n = int(input())

for _ in range(n):
    pw = input()
    result = []
    cache = []
    cur = 0
    
    for ch in pw:
        if ch == '-':
            if result:
                result.pop()
        elif ch == '<': 
            if result:
                cache.append(result.pop())
        elif ch == '>':
            if cache:
                result.append(cache.pop())
        else:
            result.append(ch)
    result.extend(reversed(cache))
        
    print("".join(result))