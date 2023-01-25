import sys
import heapq

if __name__ == "__main__":
    word = list(input().strip())
    heap = [(ch, i) for i, ch in enumerate(word)]
    heapq.heapify(heap)
    
    answer = [' ' for _ in range(len(heap))]
    
    while heap:
        ch, idx = heapq.heappop(heap)
        answer[idx] = ch
        print("".join(answer).strip())