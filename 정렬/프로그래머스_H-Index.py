def solution(citations):
    citations.sort()
    for idx in range(len(citations)):
        if citations[len(citations)-idx-1] <= idx:
            return idx
    return len(citations)

print(solution([3, 0, 6, 1, 5]))