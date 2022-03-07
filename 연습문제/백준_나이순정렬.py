num = int(input())
member = []

for i in range(num):
    age, name = input().split(" ")
    member.append((int(age), i, name))
    
member.sort(key = lambda x: (x[0], x[1]))

for m in member:
    print(m[0], m[2])