# JEAN's solution
# def solution(name):
#     answer = 0
#     length = len(name)
#     name = list(name)
#     user_name = ['A'] * length
#     i=0
    
#     while True:
#         user_name[i] = name[i]
        
#         answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i])+1)
#         if name == user_name:
#             break

#         for j in range(1, length):
#             if name[(i+j)%length] != user_name[(i+j)%length]:
#                 i = (i+j)%length
#                 answer += j
#                 break
#             if name[(length+i-j)%length] != user_name[(length+i-j)%length]:
#                 i = (length+i-j) %length
#                 answer += j
#                 break
    
#     return answer

# pythonic 

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next_idx = 0
    
    for idx, ch in  enumerate(name):
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
        
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        min_move = min(min_move, idx+idx+len(name)-next_idx)
    answer += min_move
        
    return answer
    
print(solution("JEROEN"))
print(solution("JAN"))