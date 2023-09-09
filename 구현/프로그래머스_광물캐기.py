def calc_tired(m):
    cost = {"diamond": 25, "iron": 5, "stone": 1}
    return sum([cost[n] for n in m])

def solution(picks, minerals):
    cost_dict = {
        0:{"diamond": 1, "iron": 1, "stone": 1},
        1:{"diamond": 5, "iron": 1, "stone": 1},
        2:{"diamond": 25, "iron": 5, "stone": 1},
    }
    answer = 0
    
    tired = []
    
    for i in range(0, min(sum(picks*5),len(minerals)), 5):
        tired.append(minerals[i:i+5])
    
    tired.sort(key=lambda x: -calc_tired(x))
    
    for i in range(3):
        for _ in range(picks[i]):
            if tired:
                answer += sum([cost_dict[i][arr] for arr in tired.pop(0)])
                
    return answer

if __name__ == "__main__":
    print(solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]), 12)
    print(solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]), 50)
    print(solution([1, 1, 0],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone", "iron", "iron", "diamond", "diamond"]), 14)