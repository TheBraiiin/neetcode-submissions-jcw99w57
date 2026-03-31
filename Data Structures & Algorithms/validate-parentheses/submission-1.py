class Solution:
    def isValid(self, s: str) -> bool:
        
        paren = {}
        paren[')'] = '('
        paren['}'] = '{'
        paren[']'] = '['

        stack = []

        for c in s:
            if c not in paren:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != paren[c]:
                return False 

        return len(stack) == 0
                
 #} }
        