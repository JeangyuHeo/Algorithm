class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        length = len(candidates)
        
        def dfs(total: int, nums: List[int]):
            if total == target:
                tmp = sorted(nums[:])
                if tmp not in answer:
                    answer.append(tmp)
                return
            elif total > target:
                return
            
            for i in range(length):
                dfs(total+candidates[i], nums + [candidates[i]])
                
        dfs(0, [])
        
        return answer