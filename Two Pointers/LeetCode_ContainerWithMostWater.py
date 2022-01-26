class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start = 0
        end = len(height)-1
        
        while start < end:
            answer = max(answer, (end-start) * min(height[start], height[end]))
            
            if height[start]>height[end]:
                end-=1
            else:
                start+=1
            
        return answer