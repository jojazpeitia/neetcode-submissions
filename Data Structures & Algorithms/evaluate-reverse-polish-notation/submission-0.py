class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # implement using a stack!!

        # stuff to be careful for
        # when subracting make sure its not subtracted in the order of pop since its backwards

        # when dividing make sure to round towards zero (truncate the decimal point)
        # ^ DONT DO FLOOR DIVISION

        stack = []

        for value in tokens:

            if value == "+":
                stack.append(stack.pop() + stack.pop())
            elif value == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif value == "*":
                stack.append(stack.pop() * stack.pop())
            elif value == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(value))

        return stack[-1]
