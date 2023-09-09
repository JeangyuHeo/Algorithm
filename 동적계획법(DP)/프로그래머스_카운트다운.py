def solution(target):
    candi = [i for i in range(1, 21)]
    cost = {}
    
    def dp(n):
        if n == 0:
            return (0, 0)
        if n in cost:
            return cost[n]
        
        arr = []
        
        if n-50 >= 0:
            turn, cnt = dp(n-50)
            arr.append((turn+1, cnt+1))
            
        for num in candi:
            if n - num >= 0:
                turn, cnt = dp(n-num)
                arr.append((turn+1, cnt+1))
            if n - (2 * num) >= 0:
                turn, cnt = dp(n - (2 * num))
                arr.append((turn+1, cnt))
            if n - (3 * num) >= 0:
                turn, cnt = dp(n - (3 * num))
                arr.append((turn+1, cnt))
        
        arr.sort(key=lambda x: (x[0], -x[1]))

        cost[n] = arr[0]
        return cost[n]
    
    return list(dp(target))

if __name__ == "__main__":
    print(solution(21), [1, 0])
    print(solution(58), [2, 2])