from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    count_dict = defaultdict(set)
    report_dict = defaultdict(set)
    
    for r in report:
        fr, to = r.split()
        count_dict[to].add(fr)
        report_dict[fr].add(to)
    
    ban_id = []
    
    for key, val in count_dict.items():
        if len(list(val)) >= k:
            ban_id.append(key)
            
    for _id in id_list:
        res = 0
        for b_id in ban_id:
            if b_id in report_dict[_id]:
                res += 1
        answer.append(res)
    
    return answer

if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))