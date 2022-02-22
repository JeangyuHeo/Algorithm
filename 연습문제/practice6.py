def solution(s, keypad):
    answer = 0
    cur = keypad.find(s[0])

    for ch in s:
        if ch == keypad[cur]:
            continue
        else:
            next = keypad.find(ch)
            answer += max(next % 3, next // 3)
            cur = next

    return answer

print(solution("3999", "735194826"))