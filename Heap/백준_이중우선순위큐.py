import heapq

if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        num_command = int(input())
        max_q, min_q = [], []
        visited=[False] * num_command
        
        for i in range(num_command):
            command, num = input().split()
            num = int(num)
            if command == 'I':
                visited[i] = True
                heapq.heappush(min_q, [num, i])
                heapq.heappush(max_q, [-num, i])
                
            elif command == 'D':
                if num == 1:
                    while max_q and not visited[max_q[0][1]]:
                        heapq.heappop(max_q)
                    if max_q:
                        visited[max_q[0][1]]=False
                        heapq.heappop(max_q)
                        
                elif num == -1:
                    while min_q and not visited[min_q[0][1]]:
                        heapq.heappop(min_q)
                    if min_q:
                        visited[min_q[0][1]] = False
                        heapq.heappop(min_q)
        
        while min_q and not visited[min_q[0][1]]:
            heapq.heappop(min_q)
        while max_q and not visited[max_q[0][1]]:
            heapq.heappop(max_q)
            
        if not min_q or not max_q:
            print("EMPTY")
        else:
            print(-max_q[0][0], min_q[0][0])