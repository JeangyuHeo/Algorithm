import sys

input = sys.stdin.readline

def do_command(no, command, num):
    if command == 'L':
        dir_dict[no] = (dir_dict[no]-num) % 4
    elif command == 'R':
        dir_dict[no] = (dir_dict[no]+num) % 4
    elif command == 'F':
        x, y = pos_dict[no]
        board[x][y] = 0
        nx, ny = x+dx[dir_dict[no]], y+dy[dir_dict[no]]
        pos_dict[no] = [nx, ny]
        if not check_range(no):
            print("Robot", no, "crashes into the wall")
            exit(0)
        if board[nx][ny] != 0:
            return False
        else:
            board[nx][ny] = no
            
    return True

def check_range(no):
    x, y = pos_dict[no]
    return True if 0<x<=b and 0<y<=a else False
    
if __name__ == "__main__":
    dir_to_idx = {'N': 0, 'E':1, 'S':2, 'W':3}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    
    board = [[0 for _ in range(a+1)] for _ in range(b+1)]
    pos_dict = {}
    dir_dict = {}
    
    for i in range(1, n+1):
        x, y, dir = input().split()
        board[b-int(y)+1][int(x)] = i
        pos_dict[i] = [b-int(y)+1, int(x)]
        dir_dict[i] = dir_to_idx[dir]
        
    commands = list(input().split() for _ in range(m))
    for i in range(m):
        no, command, num = commands[i]
        no, num = int(no), int(num)
        
        if command != 'F':
            do_command(no, command, num)
        else:
            for _ in range(num):
                if not do_command(no, command, num):
                    print("Robot", no, "crashes into robot", board[pos_dict[no][0]][pos_dict[no][1]])
                    exit(0)

    print("OK")