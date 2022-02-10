class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        already = []
        
        def dfs(num, parentheses):
            if num == n:
                if parentheses not in answer:
                    answer.append(parentheses[:])
                return
            if parentheses not in already:
                already.append(parentheses)
                for i in range(n):
                    dfs(num+1, parentheses[:i] + "()" + parentheses[i:])
        
        dfs(0, "")
        
        return answer