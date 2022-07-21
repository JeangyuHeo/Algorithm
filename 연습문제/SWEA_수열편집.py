T = int(input())

for test_case in range(1, T + 1):
    n,m,l = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        splited_input = input().split()
        command = splited_input[0]
        
        if command == 'I':
            pos, num = int(splited_input[1]), int(splited_input[2])
            arr = arr[:pos] + [num] + arr[pos:]
        elif command == 'D':
            pos = int(splited_input[1])
            print(pos, arr)
            arr.pop(pos)
        elif command == 'C':
            pos, num = int(splited_input[1]), int(splited_input[2])
            arr[pos] = num
	
    ans = -1
    if len(arr) != 0:
        ans = arr[-1]

    print(f"#{test_case} {ans}", test_case, ans)