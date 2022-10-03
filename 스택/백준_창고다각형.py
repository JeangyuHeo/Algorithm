import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    blocks = []
    max_idx, max_height = 0, 1
    dest, answer = 0, 0
    
    for _ in range(n):
        idx, height = map(int, input().split())
        blocks.append((idx, height))
        
        if dest < idx:
            dest = idx
        if max_height < height:
            max_height = height
            max_idx = idx
    
    height_list = [0 for _ in range(dest+1)]
    
    for idx, height in blocks:
        height_list[idx] = height
    
    temp = 0
    
    for i in range(max_idx+1):
        if height_list[i] > temp:
            temp = height_list[i]
        answer += temp
    
    temp = 0
    for i in range(dest, max_idx, -1):
        if height_list[i] > temp:
            temp = height_list[i]
            
        answer += temp
    print(answer)