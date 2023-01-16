import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int,input().strip().split())
    heap = []
    nums = list(map(int, input().strip().split()))
    heapq.heapify(nums)
    
    for _ in range(m):
        score = 0
        for _ in range(2):
            score += heapq.heappop(nums)
        for _ in range(2):
            heapq.heappush(nums, score)
            
    print(sum(nums))