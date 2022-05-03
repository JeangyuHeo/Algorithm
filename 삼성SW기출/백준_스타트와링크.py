from itertools import combinations
import sys

input = sys.stdin.readline


def add_ability(team):
    result = 0

    for i in team:
        for j in team:
            result += ability[i][j]

    return result


if __name__ == "__main__":
    answer = 1e9
    n = int(input())
    team_n = n // 2

    ability = [list(map(int, input().split(" "))) for _ in range(n)]
    combs = list(combinations([i for i in range(n)], team_n))
    num_comb = len(combs)

    for team_1, team_2 in zip(combs[:num_comb], combs[num_comb::-1]):
        team1_ability = add_ability(team_1)
        team2_ability = add_ability(team_2)

        sub = abs(team1_ability - team2_ability)

        answer = min(sub, answer)

    print(answer)
