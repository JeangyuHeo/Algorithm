import sys
import heapq

input = sys.stdin.readline

def dijkstra():
    dist = [[1e9 for _ in range(n)] for _ in range(n)]
    
    
    pq = []
    dist[0][0] = 0
    
    heapq.heappush(pq, (board[0][0], 0, 0))
    
    while pq:
        cost, x, y = heapq.heappop(pq)

        if (x,y) == (n-1, n-1):
            print(f"Problem {idx}: {dist[x][y]}")
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0<= nx < n and 0<=ny<n:
                ncost = cost + board[nx][ny]
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(pq, (ncost, nx, ny))
        
if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    
    while True:
        idx+=1
        answer = 1e9
        n = int(input())
        if n == 0:
            break
        
        board = [list(map(int, input().split())) for _ in range(n)]
        
        dijkstra()
        
        