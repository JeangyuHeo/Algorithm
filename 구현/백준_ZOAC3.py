import sys

input = sys.stdin.readline

def calc_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

if __name__ == "__main__":
    key_dict = {
        'z':(0,0),'x':(0,1), 'c':(0,2), 'v':(0,3),'b':(0,4), 'n':(0,5), 'm':(0,6),
        'a':(1,0),'s':(1,1), 'd':(1,2), 'f':(1,3),'g':(1,4), 'h':(1,5), 'j':(1,6), 'k':(1,7), 'l':(1,8),
        'q':(2,0),'w':(2,1), 'e':(2,2), 'r':(2,3),'t':(2,4), 'y':(2,5), 'u':(2,6), 'i':(2,7), 'o':(2,8), 'p':(2,9)
    }
    right_cand = ('y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm')
    cur_l, cur_r = input().strip().split()
    word = input().strip()
    
    answer = len(word)
    
    for ch in word:
        if ch in right_cand:
            x1, y1 = key_dict[cur_r]
            cur_r = ch
        else:
            x1, y1 = key_dict[cur_l]
            cur_l = ch
            
        x2, y2 = key_dict[ch]
        answer += calc_distance(x1, y1, x2, y2)
        
    print(answer)