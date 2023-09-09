from collections import defaultdict

def solution(n, x, salary, holiday):
    salaries = defaultdict(int)
    
    for i in range(x, ((n // x) * x)+1, x):
        salaries[i] = salary
    
    for start, end in holiday[::-1]:
        for i in range(start // x * x, (end // x)*x + 1, x):
            if start< i < end:
                salaries[start-1] += salaries[i]
        salaries[start-1] += salaries[start]
        salaries[start-1] += salaries[end]
            
    return max(salaries.values())

def get_result(n,x,salary,holiday):    
    if holiday[-1][1] < n-1:
        result = (((n-1)//x)+1) * salary
        return result
    
    elif len(holiday) == 1:
        n = holiday[0][0]
        result = (((n-1)//x)+1) * salary
        return result
    
    else:
        n = holiday[-1][0]
        holiday.pop()
        return get_result(n,x,salary,holiday)
    
if __name__ == "__main__":
    print(solution(6,2,10,[[4,6]]))
    print(solution(40, 8, 100, [[8, 17], [22,32], [33,40]]))
    
    print(get_result(6,2,10,[[4,6]]))
    print(get_result(40, 8, 100, [[8, 17], [22,32], [33,40]]))
    
    print(get_result(100, 8, 100, [[8, 17], [22,32], [33,40], [41, 44], [45, 63],[64, 100]]))
    print(solution(100, 8, 100, [[8, 17], [22,32], [33,40], [41, 44], [45, 63],[64, 100]]))