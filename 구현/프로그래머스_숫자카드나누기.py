from functools import reduce

def get_gcd(a, b):
    return a if b==0 else get_gcd(b, a % b)

def solution(arrayA, arrayB):
    arrayA = sorted(set(arrayA))
    arrayB = sorted(set(arrayB))
    
    gcd_a, gcd_b = reduce(get_gcd, arrayA), reduce(get_gcd, arrayB)
    
    is_possible1, is_possible2 = False, False
    
    if all([num % gcd_b for num in arrayA]):
        is_possible2 = True
    
    if all([num % gcd_a for num in arrayB]):
        is_possible1 = True
    
    return max(gcd_a, gcd_b) if is_possible1 or is_possible2 else 0

if __name__ == "__main__":
    print(solution([10, 17], [5, 20]))
    print(solution([10, 20], [5, 17]))
    print(solution([14, 35, 119], [18, 30, 102]))