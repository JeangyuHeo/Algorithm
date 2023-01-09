def count_1(num):
    if num <= 5:
        return "11011"[:num].count("1")
    
    base = 1
    
    while 5 ** (base + 1) < num:
        base+=1
    
    section = num // (5**base)
    remainder = num % (5**base)
    
    result = section * (4**base)
    
    if section > 2:
        result -= 4**base
        
    if section == 2:
        return result
    else:
        return result + count_1(remainder)
    
def solution(n, l, r):
    return count_1(r) - count_1(l-1)

if __name__ == "__main__":
    print(solution(2, 4, 17))
    print(solution(2, 1, 5))
    print(solution(2, 2, 4))