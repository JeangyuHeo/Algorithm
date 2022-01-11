def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)

    end = len(people)-1
    
    while answer <= end:
        if ((answer != end) and (people[answer] + people[end] <= limit)):
            end-=1
        answer+=1
        
    return answer