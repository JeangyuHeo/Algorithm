import sys

input = sys.stdin.readline

def check_bending(paper:str):
    while len(paper) >= 3:
        for i in range(2, len(paper), 2):
            if paper[i-2] == paper[i]:
                return False
            
        next_paper = ""
        for i in range(1, len(paper), 2):
            next_paper+=paper[i]
        
        paper = next_paper
    return True
    
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        paper = input().strip()
        
        if check_bending(paper):
            print("YES")
        else:
            print("NO")