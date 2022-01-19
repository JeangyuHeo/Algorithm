from collections import defaultdict

def calculate_fee(fees, time):
    if time <= fees[0]:
        return fees[1]
    return fees[1] + ((time-fees[0] +fees[2] - 1)//fees[2])*fees[3]
    
def calculate_time(in_time, out_time):
    in_m = (60 * int(in_time[:2])) + int(in_time[3:])
    out_m = (60 * int(out_time[:2])) + int(out_time[3:])
    return out_m - in_m
    
def solution(fees, records):
    graph = defaultdict(list)
    answer = []

    for record in records:
        items = record.split(' ')
        graph[items[1]].append((items[0], items[2]))
    
    for key in graph.keys():
        if len(graph[key]) % 2 == 1:
            graph[key].append(("23:59","OUT"))

    graph = sorted(graph.items(), key=lambda x : x[0])
    graph = {key:val for key, val in graph}

    for key in graph.keys():
        total_time=0

        for i in range(0, len(graph[key]),2):
            total_time += calculate_time(graph[key][i][0],graph[key][i+1][0])
            
        answer.append(calculate_fee(fees, total_time))
            
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))