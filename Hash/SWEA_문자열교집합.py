T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    hash_1, hash_2 ={}, {}
    n,m = map(int, input().split())

    for s in input().split():
        hash_1[s] = True

    for s in input().split():
        hash_2[s] = True
    
    for k in hash_1.keys():
        if k in hash_2.keys():
            answer += 1
            
    print(f"#{test_case} {answer}")