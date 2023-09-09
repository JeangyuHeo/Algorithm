from functools import reduce

def solution(cards):
    visited = [False for _ in range(len(cards))]
    answer = []
    
    for idx in range(len(cards)):
        if visited[idx]:
            continue
            
        total = [idx]
        visited[idx] = True
        i = idx
        
        while cards[i] - 1 not in total:
            visited[cards[i] - 1] = True
            total.append(cards[i] - 1)
            i = cards[i] - 1
        answer.append(len(total))
    
    return 0 if len(answer) == 1 else reduce(lambda a, b: a * b, sorted(answer, reverse=True)[:2])

if __name__ == "__main__":
    print(solution([8,6,3,7,2,5,1,4]), 12)