def solution(list):
    asc = True
    des = True
    
    for i in range(1,8):
        if list[i] > list[i-1]:
            des = False
        if list[i] < list[i-1]:
            asc = False
    if asc:
        return 'ascending'
    elif des:
        return 'descending'
    else:
        return 'mixed'

item = list(map(int, input().split(' ')))
print(solution(item))