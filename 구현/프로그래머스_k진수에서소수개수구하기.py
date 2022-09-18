from math import sqrt

def trans_num(n, k):
    res = ''
    
    while n != 0:
        res = str(n % k) + res
        n = n // k
    return res

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    t_num = trans_num(n, k).split('0')
    
    for n in t_num:
        if n != '':
            if is_prime(int(n)):
                answer+= 1
    
    return answer

if __name__ == "__main__":
    print(solution(437674, 3))
    print(solution(110011, 10))