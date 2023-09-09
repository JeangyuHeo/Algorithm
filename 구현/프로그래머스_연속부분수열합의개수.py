def solution(elements):
    answer = set(elements)
    size = len(elements)
    
    for i in range(size):
        total = elements[i]
        for span in range(i+1, i + size - 1):
            total += elements[span % size]
            answer.add(total)
    
    return len(answer) + 1

if __name__ == "__main__":
    print(solution([7,9,1,1,4]), 18)