class Solution:
    def backspace(self, sentence):
        stack = []
        
        for ch in sentence:
            if ch == '#' and stack:
                stack.pop()
            else:
                if ch != '#':
                    stack.append(ch)
        return stack
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        if self.backspace(s) == self.backspace(t):
            return True
        return False