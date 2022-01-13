def solution(progresses, speeds):
    answer = []

    while progresses:
        cnt=0
        while (len(progresses)!=0 and progresses[0]>=100):
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        if cnt:
            answer.append(cnt)
        
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
    return answer

solution([93,30,55], [1,30,5])