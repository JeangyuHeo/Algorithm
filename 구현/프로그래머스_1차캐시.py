from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
        elif len(cache) == cacheSize:
            cache.pop()
            cache.appendleft(city)
            answer += 5
        else:
            cache.appendleft(city)
            answer += 5
    
    return answer

if __name__ == "__main__":
    print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))