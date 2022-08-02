T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}", end= " ")
    heap  = [0]
    n = int(input())
    
    for _ in range(n):
        splited = input().split()
        
        if splited[0] == '1':
            heap.append(int(splited[1]))
            if len(heap) == 2:
                continue
            else:
                cur = len(heap)-1
                
                while cur//2 >= 1 and heap[cur] > heap[cur//2]:
                    heap[cur], heap[cur//2] = heap[cur//2], heap[cur]
                    cur = cur // 2
            
        elif splited[0] == '2':
            if len(heap) == 1:
                print(-1, end=" ")
            else:
                print(heap[1], end=" ")
                cur = 1
                heap[cur] = -1
                while 2*cur+1 < len(heap):
                    if 2*cur <len(heap) <=2*cur+1:
                        heap[cur], heap[2*cur] = heap[2*cur], heap[cur]
                    elif heap[2*cur] < heap[2*cur+1]:
                        heap[cur], heap[2*cur+1] = heap[2*cur+1], heap[cur]
                        cur = 2*cur+1
                    else:
                        heap[cur], heap[2*cur] = heap[2*cur], heap[cur]
                        cur = 2*cur
                heap.pop(cur)
    print()