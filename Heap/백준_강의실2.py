import heapq
import sys

if __name__ == "__main__":
    input = sys.stdin.readline    
    n = int(input())
    class_info = [list(map(int, input().split())) for _ in range(n)]
    lecture = [0 for _ in range(n+1)]
    class_info.sort(key = lambda x: (x[1], x[2]))

    room = []
    
    for i in range(1,n+1):
        heapq.heappush(room, i)
    
    min_heap = []
    
    for num, start, end in class_info:
        while min_heap and min_heap[0][0] <= start:
            _, r = heapq.heappop(min_heap)
            heapq.heappush(room, r)
            
        r = heapq.heappop(room)
        heapq.heappush(min_heap, [end,r])
        lecture[num] = r
        
    print(max(lecture))
    for allocated_num in lecture[1:]:
        print(allocated_num)