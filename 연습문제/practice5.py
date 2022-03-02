def solution(plain):
    length = len(plain)
    pel = plain[:]
    rev_pel = plain[::-1]

    for i in range(length):
        if pel == rev_pel:
            break
        pel = plain + plain[i] + pel[length:]
        rev_pel = rev_pel[:i] + plain[i] + rev_pel[i:]

    return len(pel)

print(solution("abab"))
print(solution("abcde"))