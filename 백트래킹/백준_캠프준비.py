import sys

sys.setrecursionlimit(10*12)
def back_tracking(idx:int, picked:list):
    global answer
    
    if idx == N:
        if picked:
            if picked[-1]-picked[0] >= X:
                if L<=sum(picked)<=R:
                    answer += 1
        return
        
    back_tracking(idx+1, picked)
    back_tracking(idx+1, picked+[nums[idx]])
        
    
if __name__ == "__main__":
    answer = 0
    N, L, R, X = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    
    back_tracking(0, [])
    
    print(answer)