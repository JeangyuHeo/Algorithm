def add_zero(num):
    if num > 9:
        return str(num)
    else:
        return '0' + str(num)

def time_to_second(time):
    split_time = list(map(int, time.split(':')))
    return split_time[0] * 3600 + split_time[1] * 60 + split_time[2]

def second_to_time(second):
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    
    return add_zero(hour) + ':' + add_zero(minute) + ':' + add_zero(second)
    
def solution(play_time, adv_time, logs):
    answer = ''
    
    play_time, adv_time = time_to_second(play_time), time_to_second(adv_time)
    all_play_time = [0 for _ in range(play_time+1)]
    
    for log in logs:
        start, end = map(time_to_second, log.split('-'))
        all_play_time[start]+=1
        all_play_time[end]-=1
        
    for i in range(1, play_time+1):
        all_play_time[i] = all_play_time[i] + all_play_time[i-1]
        
    for i in range(1, play_time+1):
        all_play_time[i] = all_play_time[i] + all_play_time[i-1]
    
    most_view = 0
    max_time = 0
    
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if most_view < all_play_time[i] - all_play_time[i-adv_time]:
                most_view = all_play_time[i] - all_play_time[i-adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_play_time[i]:
                most_view = all_play_time[i]
                max_time = i - adv_time + 1
                
    return second_to_time(max_time)
    
if __name__ == "__main__":
    print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
    print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
    print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))