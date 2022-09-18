import math
from collections import defaultdict

def hour_to_min(s):
    hh, mm = s.split(':')
    return 60 * int(hh) + int(mm)

def calc_fee(fee, no, in_dict, out_dict):
    res = 0
    len_in = len(in_dict[no])
    len_out = len(out_dict[no])
    
    for _ in range(len_in - len_out):
        out_dict[no].append(60*23 + 59)
        
    for i in range(len_in):
        res += out_dict[no][i] - in_dict[no][i]
    
    print(res)
    
    if res <= fee[0]:
        return fee[1]
    else:
        print(fee[1], res - fee[0], fee[2], fee[3])
        return fee[1] + math.ceil((res - fee[0]) / fee[2]) * fee[3]

def solution(fees, records):
    in_dict, out_dict = defaultdict(list), defaultdict(list)
    no_list = []
    answer = []
    
    for record in records:
        time, no, state = record.split()
        
        if no not in no_list:
            no_list.append(no)
        
        if state == "IN":
            in_dict[no].append(hour_to_min(time))
        else:
            out_dict[no].append(hour_to_min(time))
    
    for i in sorted(no_list):
        answer.append(calc_fee(fees, i, in_dict, out_dict))
    
    return answer