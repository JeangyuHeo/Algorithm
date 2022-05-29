import heapq

if __name__ == "__main__":
    answer = 0
    n, m = map(int,input().split())
    time = sorted(list(map(int, input().split())), reverse=True)
    socket = [0 for _ in range(m)]
    
    while time:
        front = heapq.heappop(socket)
        front += time.pop(0)
        heapq.heappush(socket, front)

    print(max(socket))