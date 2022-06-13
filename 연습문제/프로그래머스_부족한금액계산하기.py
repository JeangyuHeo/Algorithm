def solution(price, money, count):
    total = 0
    
    for i in range(1, count+1):
        total += price * i

    return total - money if total - money >= 0 else 0

if __name__ == "__main__":
    print(solution(3, 20, 4))