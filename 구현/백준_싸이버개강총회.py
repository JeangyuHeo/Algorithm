import sys
from collections import defaultdict

input = sys.stdin.readline

def time_to_minute(time):
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)
    
if __name__ == "__main__":
    s, e, q = map(time_to_minute, input().strip().split())
    checking = defaultdict(lambda: False)
    answer = 0
    
    while True:
        try:
            time, nickname = input().strip().split()
            time = time_to_minute(time)
            
            if time <= s:
                checking[nickname] = True
            elif e <= time <= q and checking[nickname]:
                answer += 1
                checking[nickname] = False
        except:
            break
        
    print(answer)