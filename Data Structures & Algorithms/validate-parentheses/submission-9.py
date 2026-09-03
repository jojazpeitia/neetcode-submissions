class Solution:
    def isValid(self, s: str) -> bool:

        symbols = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        stack = []


        for c in s: 
            if c not in symbols:
                stack.append(c)
            
            if c in symbols:
                if stack and stack[-1] == symbols[c]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


        
        