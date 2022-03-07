num = int(input())

points = []

for _ in range(num):
    x, y = map(int, input().split(' '))
    points.append((x,y))
    
points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    print(x,y)