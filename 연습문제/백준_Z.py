N, R, C = map(int, input().split(" "))
res = 0

while N > 1:
    size = (2**N) // 2
    
    if R < size and C <size:
        pass
    elif R < size and C>= size:
        res += size ** 2
        C -= size
    elif R >= size and C < size:
        res += size ** 2 * 2
        R -= size
    elif R >= size and C >= size:
        res += size ** 2 * 3
        R-=size
        C-=size
    N -= 1
    
if R==0 and C ==0:
    print(res)
elif R ==0 and C ==1:
    print(res+1)
elif R==1 and C==0:
    print(res+2)
elif R==1 and C==1:
    print(res+3)