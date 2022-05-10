
if __name__ == "__main__":
    m,n,p = map(int, input().split())
    board = [input() for _ in range(m)]
    player_dps = {}
    
    for _ in range(p):
        player, dps = input().split()
        player_dps[player] = int(dps)
    
    boss_hp = int(input())