def rotate_cube(base):
    # 시계 방향
    # 0 윗, 1 뒷, 2 아, 3 앞, 4 왼, 5 오
    if base == 'U':
        front, a,b,c,d = cube[0], cube[4], cube[3], cube[5], cube[1]
    elif base == 'D':
        front, a,b,c,d = cube[2], cube[1], cube[5], cube[3], cube[4]
    elif base == 'F':
        front, a,b,c,d = cube[3], cube[0], cube[4], cube[2], cube[5]
    elif base == 'B':
        front, a,b,c,d = cube[1], cube[5], cube[2], cube[4], cube[0]
    elif base == 'L':
        front, a,b,c,d = cube[4], cube[3], cube[0], cube[1], cube[2]
    else:
        front, a,b,c,d = cube[5], cube[2], cube[1], cube[0], cube[3]
        
    front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0], front[0][0], front[0][1] = \
        front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0]
 
    a[2][2], a[2][1], a[2][0], b[2][0], b[1][0], b[0][0], c[0][2], c[1][2], c[2][2], d[0][0], d[0][1], d[0][2] = \
        b[2][0], b[1][0], b[0][0], c[0][2], c[1][2], c[2][2], d[0][0], d[0][1], d[0][2], a[2][2], a[2][1], a[2][0]
        
if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        cube = [
            [ # 0 윗면
                ['w','w','w'],
                ['w','w','w'],
                ['w','w','w']
            ],
            [ # 1 뒷면
                ['o','o','o'],
                ['o','o','o'],
                ['o','o','o'],
            ],
            [ # 2 아랫면
                ['y','y','y'],
                ['y','y','y'],
                ['y','y','y'],
            ],
            [ # 3 앞면
                ['r','r','r'],
                ['r','r','r'],
                ['r','r','r'],
            ],
            [ # 4 왼쪽
                ['g','g','g'],
                ['g','g','g'],
                ['g','g','g'],
            ],
            [ # 5 오른쪽
                ['b','b','b'],
                ['b','b','b'],
                ['b','b','b'],
            ],
        ]
        
        num = int(input())
        rotate_list = input().split()
        
        for base, dir in rotate_list:
            rotate_cube(base)
            if dir == '-':
                rotate_cube(base)
                rotate_cube(base)
    
        for i in range(3):
            print(''.join(j for j in cube[0][i]))