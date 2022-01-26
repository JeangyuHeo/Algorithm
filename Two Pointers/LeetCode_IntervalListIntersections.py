class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        firstlist_length = len(firstList)
        secondlist_length = len(secondList)
        
        A = 0
        B = 0
        
        while A < firstlist_length and B < secondlist_length:
            start = max(firstList[A][0], secondList[B][0])
            end = min(firstList[A][1], secondList[B][1])
            
            if start <= end:
                answer.append([start, end])
            
            if end == firstList[A][1]:
                A+=1
            else:
                B+=1
                
        return answer