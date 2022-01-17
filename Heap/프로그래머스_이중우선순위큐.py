def solution(operations):
    q=[]
    
    for oper in operations:
        op_list = oper.split()
        
        if op_list[0] == 'I':
            q.append(int(op_list[1]))
        elif op_list[1] == '1' and q:
            q.pop(0)
        elif op_list[1] == '-1' and q:
            q.pop()
        
        q.sort(reverse=True)
    if len(q)==0:
        return [0,0]
    
    return [q[0], q[-1]]

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
	