def solution(cards):
    length = len(cards)
    dp_kero, dp_bero = [], []

    def dp_init(dp ,start):
            for idx, i in enumerate(range(start, length, 2)):
                if i < 2:
                    dp.append(cards[i]) 
                else:
                    dp.append(cards[i] + dp[idx-1])

    dp_init(dp_kero, 0)
    dp_init(dp_bero, 1)

    print(dp_kero, dp_bero)
    print("new")
    for i in range(length):
        if i % 2:
            print("홀")
            kero = dp_kero[i//2] + dp_bero[-1] - dp_bero[i//2]
            bero = dp_bero[i//2] - cards[i] + dp_kero[-1] - dp_kero[i//2]
        else:
            print("짝")
            kero = dp_kero[i//2] - cards[i] + dp_bero[-1]
            bero = dp_bero[i//2] + dp_kero[-1]
        print(kero, bero)
        if kero == bero:
            return i+1

    return -1

print(solution([2,5,3,1]))
print(solution([2,4,6,3,4]))
print(solution([2,5,2,7,8,4]))