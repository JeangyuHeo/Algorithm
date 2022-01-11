# def solution(number, k):
#     number = list(number)
#     answer = number[k:]
    
#     for i in range(k-1,-1,-1):
#         j=0
#         while True:
#             if number[i] >= answer[j]:
#                 answer[j],number[i] = number[i], answer[j]
#                 j+=1
#             else:
#                 break
    
#     return "".join(answer)

def solution(number, k):
    answer = []
    
    for num in number:
        while k>0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))