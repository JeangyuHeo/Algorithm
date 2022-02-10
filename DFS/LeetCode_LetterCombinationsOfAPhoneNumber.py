class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        
        num_to_ch = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def dfs(i, remain, orders):
            if len(digits) == i:
                answer.append(orders[:])
                return

            cur = remain[i]
            
            for ch in cur:
                dfs(i+1, remain, orders+ch)
                
        remain = [num_to_ch[num] for num in digits]
        
        dfs(0, remain, "")
        
        return [] if len(answer) == 1 else answer