from collections import defaultdict
import bisect

def dfs_dict(dic, info, case):
    if len(case) == 4:
        key = ''
        for i in range(len(case)):
            if case[i]:
                key+=info[i]
            else:
                key+='-'
        dic[key].append(int(info[-1]))
        return
    else:
        dfs_dict(dic, info, case + [True])
        dfs_dict(dic, info, case + [False])

def make_dict(dic, info):
    
    for i in info:
        i_list = i.split()
        dfs_dict(dic, i_list,[])

    for key in dic.keys():
            dic[key].sort()
    
def solution(info, query):
    answer = [] 
    info_dict = defaultdict(list)
    
    make_dict(info_dict, info)

    for q in query:
        count = 0
        q_list = [a for a in q.split() if a != 'and']
        joined = "".join(q_list[:-1])
        size = len(info_dict[joined])
        
        answer.append(size - bisect.bisect_left(info_dict[joined], int(q_list[-1]), lo=0, hi=size))
            
    return answer