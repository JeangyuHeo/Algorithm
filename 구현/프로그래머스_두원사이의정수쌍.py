from math import floor, ceil

def solution(r1, r2):
    answer = r2 - r1 + 1
    
    for x in range(1, r2):
        top_y = floor(((r2 ** 2) - (x ** 2))**(1/2))
        bot_y = ceil(((r1 ** 2) - (x ** 2)) ** (1/2)) if r1 > x else 0
        
        if bot_y != 0:
            answer += top_y - bot_y + 1
        else:
            answer += top_y - bot_y
    
    return answer * 4

if __name__ == "__main__":
    print(solution(2, 3))
    print(solution(4, 10))