# 1 시계, -1 반시계
def rotate(num, way):
    if way == 1:
        tmp = gears[num][-1]
        for i in range(7,0,-1):
            gears[num][i] = gears[num][i-1]
        gears[num][0] = tmp

    else:
        tmp = gears[num][0]
        for i in range(7):
            gears[num][i] = gears[num][i+1]
        gears[num][-1] = tmp 

    
# 왼쪽 2, 오른쪽 6
def check_neighbor(num, dir, way):
    if 0 <= num + dir < 4:
        if dir == 1:
            if gears[num+dir][6] != gears[num][2]:
                check_neighbor(num+dir, dir, -way)
                rotate(num+dir,-way)
        else:
            if gears[num][6] != gears[num+dir][2]:
                check_neighbor(num+dir, dir, -way)
                rotate(num+dir, -way)
                
def solution():
    for num, way in rotates:
        check_neighbor(num-1, -1, way)
        check_neighbor(num-1, 1, way)
        rotate(num-1, way)
        
    return sum([2**i * gears[i][0] for i in range(4)])

if __name__ == "__main__":
    gears = [[int(a) for a in input()] for _ in range(4)]
    k = int(input())
    
    rotates = [list(map(int, input().split(' '))) for _ in range(k)]
    
    print(solution())