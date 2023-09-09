dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def is_near(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2)) <= 3

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def make_way(x, y):
    global move_limit, turn_cnt, mode, cnt
    result = []

    if turn_cnt == 2:
        turn_cnt = 0
        move_limit += 1

    if cnt < move_limit:
        result = [x + dx[mode%4], y + dy[mode%4]]
        cnt+= 1
    if cnt == move_limit:
        mode += 1
        cnt = 0
        turn_cnt += 1
    
    return result, mode % 4


def runner_move(x, y, d):
    nx, ny = x+dx[d], y+dy[d]

    if not in_range(nx, ny):
        d = (d + 2) % 4
        nx, ny = x+dx[d], y+dy[d]

    if [nx, ny] == tagger:
        return [x, y, d]

    return [nx, ny, d]

def catch(x, y, d):
    result = 0
    candi = [(x,y)]

    for i in range(1, 3):
        nx, ny = x+(dx[d]*i), y+(dy[d]*i)
        if in_range(nx, ny):
            candi.append((nx, ny))

    for cand_x, cand_y in candi:
        if (cand_x, cand_y) in tree:
            continue
        for i in range(len(runner)-1, -1, -1):
            run_x, run_y, di = runner[i]
            if (cand_x, cand_y) == (run_x, run_y):
                # print(cand_x, cand_y)
                result += 1
                runner.pop(i)
    return result

def get_index(item):
    return int(item) - 1

if __name__ == "__main__":
    answer = 0
    n, m, h, k = map(int, input().split())
    runner = [list(map(int, input().split())) for _ in range(m)]
    runner = [[x-1, y-1, 1] if d == 1 else [x-1, y-1, 2] for x, y, d in runner]
    tree = [tuple(map(get_index, input().split())) for _ in range(h)]
    tagger = [n // 2, n // 2]

    move_st, d_list = [tagger], [0]
    move_limit, mode, turn_cnt, cnt = 1, 0, 0, 0
    
    for i in range(n**2-1):
        tagger, d = make_way(*tagger)
        move_st.append(tagger)
        d_list.append(d)

    tagger_idx = 0
    tagger_dir = 1

    move_limit, mode, turn_cnt, cnt = 1, 0, 0, 0

    tagger = [n // 2, n // 2]
    for i in range(k):
        for j in range(len(runner)):
            if is_near(tagger[0], tagger[1], runner[j][0], runner[j][1]):
                runner[j] = runner_move(*runner[j])
        
        if tagger_idx == len(move_st)-1:
            tagger_dir = -1
        elif tagger_idx == 0:
            tagger_dir = 1

        tagger_idx += tagger_dir
        tagger = move_st[tagger_idx]
        
        if (i // (n ** 2 -1)) % 2 == 1:
            d = d_list[tagger_idx-1]
            d = (d+2) % 4
        else:
            d = d_list[tagger_idx]
        
        cat_num = catch(tagger[0], tagger[1], d)
        answer += (i+1) * cat_num
        
    print(answer)