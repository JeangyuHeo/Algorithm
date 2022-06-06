if __name__ =="__main__":
    ch_hp = 0
    cur_hp = 0
    ch_damage = 0
    n, char_atk = map(int, input().split())
    room_info = [list(map(int, input().split())) for _ in range(n)]
    

    for mode, damage, hp in room_info:
        
        if mode == 1:
            attack_num = (hp // char_atk)
            if not hp % char_atk:
                ch_damage = -damage * (attack_num - 1)
            else:
                ch_damage = -damage * attack_num
        else:
            char_atk += damage
            ch_damage = hp
            
        cur_hp += ch_damage
        
        if cur_hp > 0:
            cur_hp = 0
            
        ch_hp = max(ch_hp, abs(cur_hp))
        
    print(ch_hp+1)