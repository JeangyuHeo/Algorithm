def solution(survey, choices):
    point_dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    len_sur = len(survey)
    answer = ''
    
    for i in range(len_sur):
        point = choices[i] - 4
        
        if point < 0:
            point_dict[survey[i][0]] += -point
        elif point > 0:
            point_dict[survey[i][1]] += point
    
    print(point_dict)
    
    if point_dict['R'] >= point_dict['T']:
        answer+='R'
    elif point_dict['R'] < point_dict['T']:
        answer+='T'
    
    if point_dict['C'] >= point_dict['F']:
        answer+='C'
    elif point_dict['C'] < point_dict['F']:
        answer+='F'
        
    if point_dict['J'] >= point_dict['M']:
        answer+='J'
    elif point_dict['J'] < point_dict['M']:
        answer+='M'
        
    if point_dict['A'] >= point_dict['N']:
        answer+='A'
    elif point_dict['A'] < point_dict['N']:
        answer+='N'
        
    return answer

if __name__ == "__main__":
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5,3,2,7,5]))
    print(solution(["TR", "RT", "TR"], [7,1,3]))