import sys

input = sys.stdin.readline

def back_tracking(count, start, sum):
    global visited, answer
    
    if count == n:
        if sum not in visited:
            visited[sum] = True
            answer += 1        
        return
    

    for i, num in enumerate(nums[start:]):
        back_tracking(count+1, start+i, sum+num)
    
if __name__ == "__main__":
    answer = 0
    n = int(input())
    visited = {}
    nums = [1,5,10,50]
    
    back_tracking(0,0,0)
    print(answer)