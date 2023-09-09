def calc_next(num):
    result = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        result.append(num)
            
    return result

def solution(k, ranges):
    answer = []
    
    heights = calc_next(k)
    areas = [(heights[i] + heights[i+1]) / 2 for i in range(len(heights)-1)]
    len_area = len(areas)
    
    for x, y in ranges:
        if x > len_area + y:
            answer.append(-1.0)
        elif x == len_area + y:
            answer.append(0.0)
        else:
            answer.append(sum(areas[x:len(areas) + y]))
    
    return answer

if __name__ == "__main__":
    print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))