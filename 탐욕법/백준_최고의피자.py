import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dough_price, topping_price = map(int,input().strip().split())
    dough_calorie = int(input())
    topping_calorie = sorted([int(input()) for _ in range(n)], reverse=True)
    total_calorie, total_price = dough_calorie, dough_price
    
    answer = total_calorie // total_price
    
    for topping in topping_calorie:
        total_calorie += topping
        total_price += topping_price
    
        if answer > total_calorie // total_price:
            break
        
        else:
            answer = total_calorie // total_price
    
    print(answer)