
def get_permutations(op_list):
    len_op = len(op_list)
    visited = [False for _ in range(len_op)]
    result = []
    
    def generate(chosen):
        if len(chosen) == len_op:
            result.append(chosen)
            return
        
        for i in range(len_op):
            if not visited[i]:
                visited[i] = True
                generate(chosen + [op_list[i]])
                visited[i] = False
                
    generate([])
    
    return result
        
    
if __name__ == "__main__":
    n = int(input())
    min_ans, max_ans = 1e9, -1e9
    nums = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    op_list = []
    
    for i in range(4):
        for _ in range(opers[i]):
            op_list.append(i)
    
    
    for per in get_permutations(op_list):
        tmp=0
        for i in range(n):
            if i == 0:
                tmp = nums[i]
            else:
                if per[i-1] == 0:
                    tmp += nums[i]
                elif per[i-1] == 1:
                    tmp -= nums[i]
                elif per[i-1] == 2:
                    tmp *= nums[i]
                elif per[i-1] == 3:
                    if tmp < 0:
                        tmp = - (abs(tmp) // nums[i])
                    else:
                        tmp //= nums[i]
                        
        if tmp < min_ans:
            min_ans = tmp
        if tmp > max_ans:
            max_ans = tmp
    
    print(max_ans)
    print(min_ans)