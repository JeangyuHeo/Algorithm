from functools import reduce

if __name__ == "__main__":
    answer = 0
    num = int(input())
    
    factorial_num = reduce(lambda acc, cur: acc*cur, [i for i in range(2, num+1)], 1)
    
    while factorial_num % 10 == 0:
        factorial_num //= 10
        answer += 1
        
    print(answer)