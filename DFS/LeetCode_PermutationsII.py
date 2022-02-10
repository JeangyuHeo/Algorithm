class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        answer = []
        visited = [0] * length
        
        def dfs(num, pers):
            if num == length:
                if pers not in answer:
                    answer.append(pers[:])
                return
        
            for i in range(length):
                if not visited[i]:
                    visited[i] = 1
                    dfs(num+1, pers + [nums[i]])
                    visited[i] = 0
                    
        dfs(0, [])
        
        return answer