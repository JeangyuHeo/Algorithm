import sys

input = sys.stdin.readline

            
if __name__ == "__main__":
    answer = []
    n = int(input())
    m = int(input())
    
    arr = [[False for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        big, small = map(int, input().split())
        arr[big-1][small-1] = True
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][k] and arr[k][j]:
                    arr[i][j] = True
                    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i!=j and not arr[i][j] and not arr[j][i]:
                cnt+=1
        print(cnt)