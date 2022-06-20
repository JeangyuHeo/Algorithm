from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())
    q = deque([[input().strip().count('T'), 0]])
    visited = {}
    
    while q:
        tail, cnt = q.popleft()
        head = n - tail
        
        if tail == n:
            print(cnt)
            break
        
        for i in range(k):
            back_to_front = i
            front_to_back = k-i
            
            if back_to_front <= tail and front_to_back <= head:
                if tail - back_to_front + front_to_back not in visited:
                    visited[tail - back_to_front + front_to_back] = True
                    q.append([tail - back_to_front + front_to_back, cnt+1])
    else:
        print(-1)