class Solution:
    def isValid(self, s: str) -> bool:

        check = {
            ')':'(', 
            '}':'{',
            ']':'['
        }

        stack = []

        # if its open parantheses with just push that thang

        for c in s:

            if c not in check:
                stack.append(c)
            else:
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False

        if stack: 
            return False 
        else: 
            return True
        