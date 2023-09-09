from collections import Counter

def solution(topping):
    answer = 0
    count_topping = Counter(topping)
    
    chulsoo = set()
    
    while topping:
        top = topping.pop()
        
        chulsoo.add(top)
        
        if count_topping[top] > 1:
            count_topping[top] -= 1
        
        else:
            del count_topping[top]
        
        if len(chulsoo) == len(count_topping.keys()):
            answer += 1
    
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 1, 3, 1, 4, 1, 2]), 2)
    print(solution([1, 2, 3, 1, 4]), 0)