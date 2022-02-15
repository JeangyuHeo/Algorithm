from itertools import combinations

def calc_avg(arr):
    return sum(arr) // len(arr)

def solution(prices, d, k):
    cases = []
    length = len(prices)
    prices.sort()

    #case1
    if prices[-1] - prices[0] <= d:
        return calc_avg(prices)

    #case2
    if prices[-2] - prices[1] <= d:
        return calc_avg(prices[1:-1])

    #case3
    for comb in combinations(prices, k):
        tmp = sorted(list(comb))
        if tmp not in cases:
            cases.append(tmp)

    min_val = 1e9

    for case in cases:
        if case[-1] - case[0] <= d:
            min_val = min(min_val, calc_avg(case))
    if min_val != 1e9:
        return min_val

    #case4
    if length % 2 ==0:
        return prices[(length // 2) - 1]
    else:
        return prices[length // 2]



# Test cases
# result : 6
prices = [4, 5, 6, 7, 8]
d = 4
k = 3
print(solution(prices, d, k))
# result : 6
prices = [4, 5, 6, 7, 8]
d = 2
k = 1
print(solution(prices, d, k))

# result : 4
prices = [4, 5, 6, 7, 8]
d = 1
k = 2
print(solution(prices, d, k))

# result : 6
prices = [8, 4, 5, 7, 6]
d = 1
k = 3
print(solution(prices, d, k))

# result : 1
prices = [1, 8, 1, 8, 1, 8]
d = 6
k = 4
print(solution(prices, d, k))